// Some definitions presupposed by pandoc's typst output.
#let blockquote(body) = [
  #set text( size: 0.92em )
  #block(inset: (left: 1.5em, top: 0.2em, bottom: 0.2em))[#body]
]

#let horizontalrule = [
  #line(start: (25%,0%), end: (75%,0%))
]

#let endnote(num, contents) = [
  #stack(dir: ltr, spacing: 3pt, super[#num], contents)
]

#show terms: it => {
  it.children
    .map(child => [
      #strong[#child.term]
      #block(inset: (left: 1.5em, top: -0.4em))[#child.description]
      ])
    .join()
}

// Some quarto-specific definitions.

#show raw.where(block: true): block.with(
    fill: luma(230), 
    width: 100%, 
    inset: 8pt, 
    radius: 2pt
  )

#let block_with_new_content(old_block, new_content) = {
  let d = (:)
  let fields = old_block.fields()
  fields.remove("body")
  if fields.at("below", default: none) != none {
    // TODO: this is a hack because below is a "synthesized element"
    // according to the experts in the typst discord...
    fields.below = fields.below.amount
  }
  return block.with(..fields)(new_content)
}

#let empty(v) = {
  if type(v) == "string" {
    // two dollar signs here because we're technically inside
    // a Pandoc template :grimace:
    v.matches(regex("^\\s*$")).at(0, default: none) != none
  } else if type(v) == "content" {
    if v.at("text", default: none) != none {
      return empty(v.text)
    }
    for child in v.at("children", default: ()) {
      if not empty(child) {
        return false
      }
    }
    return true
  }

}

// Subfloats
// This is a technique that we adapted from https://github.com/tingerrr/subpar/
#let quartosubfloatcounter = counter("quartosubfloatcounter")

#let quarto_super(
  kind: str,
  caption: none,
  label: none,
  supplement: str,
  position: none,
  subrefnumbering: "1a",
  subcapnumbering: "(a)",
  body,
) = {
  context {
    let figcounter = counter(figure.where(kind: kind))
    let n-super = figcounter.get().first() + 1
    set figure.caption(position: position)
    [#figure(
      kind: kind,
      supplement: supplement,
      caption: caption,
      {
        show figure.where(kind: kind): set figure(numbering: _ => numbering(subrefnumbering, n-super, quartosubfloatcounter.get().first() + 1))
        show figure.where(kind: kind): set figure.caption(position: position)

        show figure: it => {
          let num = numbering(subcapnumbering, n-super, quartosubfloatcounter.get().first() + 1)
          show figure.caption: it => {
            num.slice(2) // I don't understand why the numbering contains output that it really shouldn't, but this fixes it shrug?
            [ ]
            it.body
          }

          quartosubfloatcounter.step()
          it
          counter(figure.where(kind: it.kind)).update(n => n - 1)
        }

        quartosubfloatcounter.update(0)
        body
      }
    )#label]
  }
}

// callout rendering
// this is a figure show rule because callouts are crossreferenceable
#show figure: it => {
  if type(it.kind) != "string" {
    return it
  }
  let kind_match = it.kind.matches(regex("^quarto-callout-(.*)")).at(0, default: none)
  if kind_match == none {
    return it
  }
  let kind = kind_match.captures.at(0, default: "other")
  kind = upper(kind.first()) + kind.slice(1)
  // now we pull apart the callout and reassemble it with the crossref name and counter

  // when we cleanup pandoc's emitted code to avoid spaces this will have to change
  let old_callout = it.body.children.at(1).body.children.at(1)
  let old_title_block = old_callout.body.children.at(0)
  let old_title = old_title_block.body.body.children.at(2)

  // TODO use custom separator if available
  let new_title = if empty(old_title) {
    [#kind #it.counter.display()]
  } else {
    [#kind #it.counter.display(): #old_title]
  }

  let new_title_block = block_with_new_content(
    old_title_block, 
    block_with_new_content(
      old_title_block.body, 
      old_title_block.body.body.children.at(0) +
      old_title_block.body.body.children.at(1) +
      new_title))

  block_with_new_content(old_callout,
    new_title_block +
    old_callout.body.children.at(1))
}

// 2023-10-09: #fa-icon("fa-info") is not working, so we'll eval "#fa-info()" instead
#let callout(body: [], title: "Callout", background_color: rgb("#dddddd"), icon: none, icon_color: black) = {
  block(
    breakable: false, 
    fill: background_color, 
    stroke: (paint: icon_color, thickness: 0.5pt, cap: "round"), 
    width: 100%, 
    radius: 2pt,
    block(
      inset: 1pt,
      width: 100%, 
      below: 0pt, 
      block(
        fill: background_color, 
        width: 100%, 
        inset: 8pt)[#text(icon_color, weight: 900)[#icon] #title]) +
      if(body != []){
        block(
          inset: 1pt, 
          width: 100%, 
          block(fill: white, width: 100%, inset: 8pt, body))
      }
    )
}



#let article(
  title: none,
  authors: none,
  date: none,
  abstract: none,
  abstract-title: none,
  cols: 1,
  margin: (x: 1.25in, y: 1.25in),
  paper: "us-letter",
  lang: "en",
  region: "US",
  font: (),
  fontsize: 11pt,
  sectionnumbering: none,
  toc: false,
  toc_title: none,
  toc_depth: none,
  toc_indent: 1.5em,
  doc,
) = {
  set page(
    paper: paper,
    margin: margin,
    numbering: "1",
  )
  set par(justify: true)
  set text(lang: lang,
           region: region,
           font: font,
           size: fontsize)
  set heading(numbering: sectionnumbering)

  if title != none {
    align(center)[#block(inset: 2em)[
      #text(weight: "bold", size: 1.5em)[#title]
    ]]
  }

  if authors != none {
    let count = authors.len()
    let ncols = calc.min(count, 3)
    grid(
      columns: (1fr,) * ncols,
      row-gutter: 1.5em,
      ..authors.map(author =>
          align(center)[
            #author.name \
            #author.affiliation \
            #author.email
          ]
      )
    )
  }

  if date != none {
    align(center)[#block(inset: 1em)[
      #date
    ]]
  }

  if abstract != none {
    block(inset: 2em)[
    #text(weight: "semibold")[#abstract-title] #h(1em) #abstract
    ]
  }

  if toc {
    let title = if toc_title == none {
      auto
    } else {
      toc_title
    }
    block(above: 0em, below: 2em)[
    #outline(
      title: toc_title,
      depth: toc_depth,
      indent: toc_indent
    );
    ]
  }

  if cols == 1 {
    doc
  } else {
    columns(cols, doc)
  }
}

#set table(
  inset: 6pt,
  stroke: none
)
#show: doc => article(
  title: [LLM Time-Saving and Demand Theory],
  authors: (
    ( name: [Tom Cunningham],
      affiliation: [],
      email: [] ),
    ),
  date: [2025-11-19],
  fontsize: 11pt,
  toc_title: [Table of contents],
  toc_depth: 3,
  cols: 1,
  doc,
)


Many thanks to Elsie Jang for discussion.

== Summary
<summary>
/ I anticipate that we’re going to be arguing a lot about LLM-speedups & task substitution over the next year.: #block[
- Suppose an LLM speeds you up by a factor $beta$ on tasks that take up share $s$ of your work (pre-LLM), what’s the overall efficiency gain?
- How does the answer change if you measure the time-share $s$, #emph[after] you adjust to use LLMs?
]

/ Quick checklist\:: #block[
+ The total output gain will be between $frac(1, (1 - s) + s \/ beta)$ (if perfect complements/Amdahl) and $beta$ (perfect substitutes).

+ If the time-savings are tiny then Hulten’s theorem applies: $Delta ln y approx s ln beta$ (and for tiny changes, time-saved $approx Delta ln y$ too).

+ If the time-savings are small then you can use elasticity of substitution (there’s a closed-form expression but it’s ugly).

+ If the time-savings are large then you should use the entire area under the demand curve (i.e.~not reasonable to assume constant elasticity). Though in demand theory this relies on income effects being small, & I think a sufficient condition is that the expenditure share is small. When the expenditure share is large I’m not confident how to think about this.

+ Applying Amdahl’s law ex-ante will under-estimate productivity improvements; applying it ex-post will over-estimate productivity improvements.
]

#strong[Time savings using #emph[ex-ante] time shares]

#figure(
  align(center)[#table(
    columns: (50.49%, 16.5%, 16.5%, 16.5%),
    align: (auto,auto,auto,auto,),
    table.header([], [10% saving on 50%], [50% saving on 10%], [80% saving on 10%],),
    table.hline(),
    [$epsilon = 0$ (perfect complements/Amdahl)], [5.0%], [5.0%], [8.0%],
    [$epsilon = 1 \/ 2$ (complements)], [5.1%], [5.8%], [10.7%],
    [$epsilon = 1$ (Cobb-Douglas/Hulten)], [5.1%], [6.7%], [14.9%],
    [$epsilon arrow.r oo$ (perfect substitutes)], [10%], [50%], [80%],
  )]
  , kind: table
  )

/ Time savings using #emph[ex-post] time shares\:: #block[
#figure(
  align(center)[#table(
    columns: (46.23%, 17.92%, 17.92%, 17.92%),
    align: (auto,auto,auto,auto,),
    table.header([], [10% saving on 50%], [50% saving on 10%], [80% saving on 10%],),
    table.hline(),
    [$epsilon = 0$ (perfect complements/Amdahl)], [5.3%], [9.1%], [28.6%],
    [$epsilon = 1 \/ 2$ (complements)], [5.2%], [7.8%], [20.8%],
    [$epsilon = 1$ (Cobb-Douglas/Hulten)], [5.1%], [6.7%], [14.9%],
    [$epsilon arrow.r oo$ (perfect substitutes)], [N/A], [N/A], [N/A],
  )]
  , kind: table
  )
]

/ How these are calculated\:: #block[
- #strong["X% saving"] means task-2 productivity increases so that time-per-unit falls by factor $(1 - X)$, i.e., $beta = 1 \/ (1 - X)$. So 10% saving → $beta = 1.11$; 50% saving → $beta = 2$; 80% saving → $beta = 5$.
  - #strong["Y% of work"] means the time share on task 2 is $s = Y$.
  - #strong[Output gain] from the CES formula: $ frac(y prime, y) = ((1 - s_0) + s_0 thin beta^(epsilon - 1))^(1 \/ (epsilon - 1)) $ where $s_0$ is the #emph[ex-ante] share.
  - #strong[Time savings] = $1 - (y prime \/ y)^(- 1)$, i.e., the fraction of time saved to produce the same output.
  - #strong[Table 1:] The column header specifies the ex-ante share $s_0$ directly. Compute the output gain and convert to time savings.
  - #strong[Table 2:] The column header specifies the ex-post share $s_1$. First back out the implied ex-ante share using: $ frac(s_0, 1 - s_0) = frac(s_1, 1 - s_1) dot.op beta^(1 - epsilon) $ Then compute the true output gain using $s_0$.
  - #strong[Perfect substitutes (Table 2):] After any productivity improvement, you reallocate entirely to the better task, so the ex-post share is always 100%. Specifying it as 10% or 50% is inconsistent with optimization—hence N/A.
]

/ An analogy\: if we can turn lead into gold, what benefit do I get?: #block[
Using ex ante expenditure: my expenditure share on gold is \~0%, so my benefit is very small.

Using ex post expenditure: if gold is cheap then I’ll start buying gold cutlery. Suppose I spend \$1K on gold/year, then it makes it look like I’m getting value worth \$100K/year, which is clearly wrong.

I think the resolution is that gold has high substitutability with other goods (steel, bronze), and so demand is highly elastic. But that substitutability only appears when prices are low, so just estimating a CES function I think would get this wrong.
]

/ There are some nice crisp results from economics that apply here.: #block[
I discuss some related literature below.
]

/ Loose ends\:: #block[
- I give bounds on aggregate time-savings with a CES model below, but I’m not sure whether you might not get wider bounds if you relax the CES assumption, e.g.~with non-homotheticities so there are income effects.
]

= Model
<model>
We set up a two-task CES production problem and derive the optimal time split, the implied output, and the response to productivity changes, with limits for common special cases.

#strong[Practical implications (at a glance)]

Let $s equiv t_2^(\*)$ denote the optimal time share on task 2 (and $1 - s = t_1^(\*)$). Express all effects as log-changes $Delta ln y^(\*) = ln #h(-1em) #scale(x: 120%, y: 120%)[\(] y^(\* prime) \/ y^(\*) #scale(x: 120%, y: 120%)[\)]$ when task-2 productivity moves from $A_2$ to $A_2 prime = beta A_2$. The last column plugs in $s = 0.1$ and $beta = 2$.

#figure(
  align(center)[#table(
    columns: (24.19%, 33.02%, 21.86%, 20.93%),
    align: (auto,auto,auto,auto,),
    table.header([Case], [Output effect ($Delta ln y^(\*)$)], [Intuition], [Example $Delta ln y^(\*)$ ($s = 0.1 , med beta = 2$)],),
    table.hline(),
    [General finite change], [$frac(1, epsilon - 1) ln #h(-1em) #scale(x: 120%, y: 120%)[\(] (1 - s) + s thin beta^(epsilon - 1) #scale(x: 120%, y: 120%)[\)]$], [CES-weighted average of the shock], [$frac(1, epsilon - 1) ln #h(-1em) #scale(x: 120%, y: 120%)[\(] 0.9 + 0.1 times 2^(epsilon - 1) #scale(x: 120%, y: 120%)[\)]$ (depends on $epsilon$)],
    [Perfect substitutes ($epsilon arrow.r oo$)], [$ln beta$], [All time moves to the better task], [$approx 0.69$],
    [Cobb–Douglas ($epsilon = 1$)], [$s thin ln beta$], [Log-linear weighting by the task share], [$approx 0.069$],
    [Perfect complements ($epsilon arrow.r 0$)], [$- ln #h(-1em) #scale(x: 120%, y: 120%)[\(] (1 - s) + s \/ beta #scale(x: 120%, y: 120%)[\)]$], [Bottlenecked by the slow task], [$approx 0.051$],
    [Infinitesimal change (Hulten)], [$s thin d ln A_2$], [Percent gain equals time share on improved task], [$0.1 times ln 2 approx 0.069$],
  )]
  , kind: table
  )

#strong[Setup and parameters]

- Time endowment is $1$; choose $t_1 in [0 , 1]$ and $t_2 = 1 - t_1$.
- Productivities: $A_1 > 0$ for task $1$, $A_2 > 0$ for task $2$.
- Taste weight: $alpha in (0 , 1)$ on task $1$.
- Substitution parameter: $epsilon > 0$; take $epsilon eq.not 1$ for the algebra and then send $epsilon arrow.r 1$ for the Cobb–Douglas limit.
- Output aggregator (CES): $ y (t_1 , t_2) = (alpha (A_1 t_1)^(frac(epsilon - 1, epsilon)) + (1 - alpha) (A_2 t_2)^(frac(epsilon - 1, epsilon)))^(frac(epsilon, epsilon - 1)) . $

#strong[Assumptions]

+ Feasible set: $t_1 in [0 , 1]$, $t_2 = 1 - t_1$.
+ Parameters satisfy $A_i > 0$ and $alpha in (0 , 1)$.
+ Decision problem: choose $t_1$ to maximise $y (t_1 , 1 - t_1)$.

#strong[Proposition 1 (optimal time split).] The interior optimum is $ t_1^(\*) = frac(1, 1 + (frac(1 - alpha, alpha))^epsilon (A_2 / A_1)^(epsilon - 1)) , #h(2em) t_2^(\*) = 1 - t_1^(\*) . $

#emph[Proof (explicit)]

+ Write the Lagrangian $cal(L) = y (t_1 , t_2) + lambda (1 - t_1 - t_2)$ with $y$ as above.
+ First-order conditions (interior): $partial cal(L) \/ partial t_1 = 0$ and $partial cal(L) \/ partial t_2 = 0$ give $ lambda = alpha thin A_1^(frac(epsilon - 1, epsilon)) thin t_1^(- 1 / epsilon) thin y^(1 / epsilon) = (1 - alpha) thin A_2^(frac(epsilon - 1, epsilon)) thin t_2^(- 1 / epsilon) thin y^(1 / epsilon) . $
+ Cancel $y^(1 / epsilon)$ and rearrange to obtain $t_2 / t_1 = (frac(1 - alpha, alpha))^epsilon (A_2 / A_1)^(epsilon - 1)$.
+ Impose $t_1 + t_2 = 1$ and solve for $t_1^(\*)$; set $t_2^(\*) = 1 - t_1^(\*)$.
+ The interior solution is valid for $epsilon > 0$ with finite $A_i$; only the perfect-substitutes limit $epsilon arrow.r oo$ or $A_i arrow.r 0$ forces a corner.

#strong[Proposition 2 (indirect output).] At $t_1^(\*) , t_2^(\*)$ the output is $ y^(\*) = #scale(x: 180%, y: 180%)[\(] alpha^epsilon A_1^(epsilon - 1) + (1 - alpha)^epsilon A_2^(epsilon - 1) #scale(x: 180%, y: 180%)[\)]^(frac(1, epsilon - 1)) . $

#emph[Proof (explicit)]

+ Substitute $t_1^(\*) , t_2^(\*)$ from Proposition 1 into $y (t_1 , t_2)$.
+ Factor out $alpha^epsilon A_1^(epsilon - 1) + (1 - alpha)^epsilon A_2^(epsilon - 1)$ inside the braces; the exponent $frac(epsilon, epsilon - 1)$ collapses to the stated form.

#strong[Proposition 3 (infinitesimal productivity change).] Holding $A_1$ fixed, a small change in $A_2$ satisfies $ frac(d y^(\*), y^(\*)) = t_2^(\*) thin frac(d A_2, A_2) . $

#emph[Proof (explicit)]

+ Take $log y^(\*) = frac(1, epsilon - 1) log #scale(x: 120%, y: 120%)[\(] alpha^epsilon A_1^(epsilon - 1) + (1 - alpha)^epsilon A_2^(epsilon - 1) #scale(x: 120%, y: 120%)[\)]$.
+ Differentiate with respect to $log A_2$: $ frac(d y^(\*), y^(\*)) = frac((1 - alpha)^epsilon A_2^(epsilon - 1), alpha^epsilon A_1^(epsilon - 1) + (1 - alpha)^epsilon A_2^(epsilon - 1)) dot.op frac(d A_2, A_2) . $
+ The fraction equals $t_2^(\*)$ from Proposition 1, so the result follows.

#strong[Proposition 4 (finite productivity change on task 2).] If $A_2 prime = beta A_2$ with $beta > 0$, then $ y^(\* prime) / y^(\*) = (t_1^(\*) + (1 - t_1^(\*)) beta^(epsilon - 1))^(frac(1, epsilon - 1)) . $

#emph[Proof (explicit)]

+ Replace $A_2$ by $beta A_2$ in $y^(\*)$ from Proposition 2: $ y^(\* prime) = #scale(x: 180%, y: 180%)[\(] alpha^epsilon A_1^(epsilon - 1) + (1 - alpha)^epsilon (beta A_2)^(epsilon - 1) #scale(x: 180%, y: 180%)[\)]^(frac(1, epsilon - 1)) . $
+ Factor out the old level $y^(\*)$ to form a ratio; the remaining weights inside the braces are $t_1^(\*)$ and $t_2^(\*) = 1 - t_1^(\*)$, giving the stated expression.

#strong[Proposition 5 (canonical limits).] Take limits of Proposition 4:

- Cobb–Douglas ($epsilon arrow.r 1$): $y^(\* prime) / y^(\*) arrow.r beta^(1 - alpha)$ and $t_i^(\*)$ is unchanged.
- Perfect complements ($epsilon arrow.r 0$): $y^(\* prime) / y^(\*) arrow.r frac(1, t_1^(\*) + t_2^(\*) \/ beta)$.
- Perfect substitutes ($epsilon arrow.r oo$): $y^(\* prime) / y^(\*) arrow.r beta$ with $t_2^(\*) arrow.r 1$ if $beta A_2 > A_1$.

#emph[Proof sketch] For $epsilon arrow.r 1$ apply L’Hôpital to the CES form. For $epsilon arrow.r 0$ the CES aggregator converges to $min { A_1 t_1 , A_2 t_2 }$. For $epsilon arrow.r oo$ it converges to $max { A_1 t_1 , A_2 t_2 }$. Substitute these limits into Proposition 4 and simplify.

= Example Applications
<example-applications>
/ #cite(<anthropic2025estimatingproductivitygains>, form: "prose");: #block[
They estimate Claude saves time by 80% on certain tasks, and apply Hulten’s theorem. But Hulten’s theorem only applies for #emph[small] efficiency changes, so I believe this effectively assumes Cobb-Douglas substitution (i.e.~constant time-shares on these tasks).
]

/ #cite(<becker2025uplift>, form: "prose");: #block[
They estimate time-savings on tasks using LLMs. In this case the subjects mostly were #emph[not] using AI, but in followup studies they #emph[will] be using AI. This makes it hard to think about interpreting uplift studies over time, insofar as AI causes them to change the task distribution. It would be nice to have a good clear language here.
]

= Related Theory
<related-theory>
/ Index numbers and the "which share do you weight by?" problem: #block[
#cite(<caves1982indexnumbers>, form: "prose") formalize why productivity (or "quantity") measurement becomes an index-number problem as soon as #emph[shares move endogenously];. Their key point is that fixed-weight indices answer the wrong question when agents substitute:

- A Laspeyres-style measure (base-period weights) is biased toward #emph[understating] gains when a shock makes you reallocate toward the improved input/task, because it freezes the old bundle.

- A Paasche-style measure (end-period weights) is biased toward #emph[overstating] gains if you implicitly treat the new bundle as if it had always been purchased at the old relative prices/technologies.

- The object you actually want is a path (Divisia) integral of share-weighted growth rates; "superlative" discrete indices (e.g., Fisher/Törnqvist) are designed to approximate that integral well.

#strong[Connection to our setup:] our two-task CES makes this completely explicit. Proposition 3 is the Divisia/Hulten-style statement: $ d ln y^(\*) = t_2^(\*) thin d ln A_2 , $ so the "right weight" is the #emph[current] optimal time share $t_2^(\*)$, not a fixed pre/post share. For a finite $beta$ shock, the exact change is the integral of that weight along the adjustment path, which collapses to the closed form in Proposition 4. This is exactly the sense in which "ex‑ante Amdahl/Hulten" (freeze $t_2$ at baseline) understates and "ex‑post Hulten" (freeze $t_2$ at the endpoint) can overstate.
]

/ Consumer surplus / welfare for large "price" (time-cost) changes: #block[
#cite(<willig1976consumerssurplus>, form: "prose") defends using Marshallian consumer surplus as a welfare proxy: the area under the (Marshallian) demand curve is close to the Hicksian objects (EV/CV) when income effects are small, and Willig provides conditions/bounds under which the approximation error is limited.

#cite(<hausman1981exact>, form: "prose") shows how to compute exact welfare measures (EV/CV, deadweight loss) from an estimated demand curve by imposing integrability (i.e., that the demand actually comes from some underlying utility/expenditure function).

#cite(<deaton1980aids>, form: "prose") provides a workhorse #emph[integrable] demand system (AIDS) that flexibly captures income effects and substitution patterns while keeping welfare calculations coherent.

#strong[Connection to our setup:] if you reinterpret the model in dual form, "task outputs" ($x_i = A_i t_i$) are the "goods," and the time budget implies prices ($p_i = 1 \/ A_i$) (time per unit of task output). An LLM that raises $A_2$ by $beta$ is literally a price drop for good 2 by a factor $1 \/ beta$. For small task shares ($s = t_2^(\*)$) (your "gold is tiny in the budget" example), the Willig logic says "income-effect-like problems are muted," so simple surplus approximations are safer. When the effective budget share is not tiny—or when the shock is huge—the Hausman/Deaton-Muellbauer message is: you want an #emph[integrable system] (or in our case, an explicit aggregator like CES) so that "area under a curve" corresponds to a defensible welfare change.
]

/ Economics of time allocation (time is a scarce input with shadow prices): #block[
#cite(<deserpa1971time>, form: "prose") treats time as a fundamental scarce resource: activities require time as well as market goods, and constraints on required time generate a shadow value of time. The key conceptual result is that "time-saving" innovations matter because they relax a binding constraint, and the value of that relaxation depends on the shadow price of time and substitution across activities.

#strong[Connection to our setup:] we’re essentially running the cleanest possible DeSerpa-style problem: a single time endowment allocated across tasks, where task technologies ($A_i$) turn time into effective task output. The LLM shock is a direct relaxation of the time requirement for task 2. What DeSerpa adds conceptually is the interpretation: the welfare/productivity effect is not "minutes saved" per se, but "minutes saved #emph[valued at the shadow price of time];," and that shadow price is determined jointly with substitution across tasks—exactly what $epsilon$ is doing for us.
]

/ Task substitution and computerization as task-specific technology shocks: #block[
#cite(<autor2003skill>, form: "prose") is the empirical foundation for the modern "tasks" approach: computerization substitutes for routine tasks and complements non-routine tasks, shifting task content within occupations and generating distributional consequences (e.g., polarization). The paper’s core claim is that you cannot summarize tech change as "labor-augmenting" in the aggregate; it’s task-directed, and substitution patterns matter.

#cite(<acemoglu2011handbook>, form: "prose") synthesizes and formalizes this task-based view. A central message is that the impact of a task-specific productivity shock depends on: (i) which tasks are affected, (ii) how substitutable tasks are, and (iii) how the economy re-optimizes task assignment across workers/technologies.

#strong[Connection to our setup:] our $A_2 arrow.r.bar beta A_2$ change is exactly a "task-directed" shock. Your entire "ex‑ante vs ex‑post task share" issue is basically the same point Autor/Acemoglu-Autor emphasize: task shares are endogenous responses to technology, not fixed primitives. In our CES aggregator, that endogeneity is governed by $epsilon$: when $epsilon$ is high, reallocation is large and the "Amdahl intuition" breaks; when $epsilon$ is low, reallocation is small and Amdahl becomes accurate.
]

/ Hulten’s theorem and when first-order share-weighting breaks: #block[
#cite(<hulten1978growth>, form: "prose") shows (in a competitive, CRS setting with intermediates) that a #emph[small] productivity shock’s effect on aggregate productivity can be summarized by share-weighted sectoral TFP growth (Domar/revenue-share weights). The key takeaway is the legitimacy of first-order share weighting—but only locally.

#strong[#cite(<baqaee2019macro>, form: "prose");] pushes beyond that local logic: in production networks, micro shocks can have macro consequences and nonlinearities/higher-order terms matter, especially for large shocks or when substitution patterns interact with network structure.

#cite(<baqaeeBurstein2021incomeeffects>, form: "prose") highlights that welfare vs.~output can diverge when income effects / demand shifts are important, and that changing expenditure patterns can be central to aggregate responses (so "just Domar weights" can miss key welfare channels).

#cite(<cominLashkariMestieri2021structuralchange>, form: "prose") emphasizes that over longer horizons, relative price changes and non-homotheticities induce structural change: shares drift systematically, so you should expect "task/sector shares" to be part of the response to technology, not a nuisance.

#strong[Connection to our setup:] Proposition 3 is the Hulten logic in a two-task world (local, share-weighted). Proposition 4 is the "nonlinear / finite change" version where the share itself moves with $beta$.
]

/ Amdahl’s law as the perfect-complements benchmark: #block[
Amdahl’s law says the speedup from improving one component is bounded by the unimproved fraction.

#strong[Connection to our setup:] that’s precisely the $epsilon arrow.r 0$ (Leontief / perfect complements) limit in Proposition 5: $ y^(\* prime) / y^(\*) arrow.r frac(1, (1 - s) + s \/ beta) . $
]

/ \<!– Reallocation and aggregation across units (Olley–Pakes): #block[
#cite(<olley1996telecom>, form: "prose") shows that aggregate productivity can be decomposed into: (i) the unweighted mean productivity across firms ("within"), plus (ii) a covariance between productivity and market share ("between" / reallocation). Their empirical contribution is that changes in aggregate productivity can come as much from reallocating activity toward more productive firms as from within-firm improvements.–\>
]

= Illustrations
<illustrations>
== Indifference Curve
<indifference-curve>
#figure([
#box(image("2025-12-17-llm-time-saving-demand-theory-substitution_files/figure-typst/unnamed-chunk-1-1.svg"))
], caption: figure.caption(
position: bottom, 
[
Budget constraint and optimal allocations under different elasticities
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


== Demand Curve
<demand-curve>
#figure([
#box(image("2025-12-17-llm-time-saving-demand-theory-substitution_files/figure-typst/unnamed-chunk-2-1.svg"))
], caption: figure.caption(
position: bottom, 
[
Demand curves with different price elasticities
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)





#bibliography("ai.bib")

