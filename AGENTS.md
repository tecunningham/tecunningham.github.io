## Overview

This repo hosts the source for a personal website/blog. It includes post sources
(`.qmd`, `.md`, `.typ`, `.tex`), bibliographies (`.bib`), figures/images, and
some generated artifacts (HTML/PDF and `_cache`/`_files` outputs).

## Bibliography notes

`ai.bib` is partly machine-updated. It contains documentation at the top of the
file describing BibTeX formatting guidelines.

## Conventions

- Files named `XXX.llm.qmd` indicate documents written by an LLM.

## Quarto Markdown Notes

### Definition Lists (Pandoc/Quarto)

Quarto uses Pandoc's definition-list parsing, which is sensitive to whitespace.

Rules of thumb:

- A definition list item is `Term` followed immediately by a line starting with a single `:`. Do not put a blank line between the term and the `:` line.
- The `:` must start at the beginning of the line (column 1). If it is indented, Pandoc may treat it as a code block or part of a different list.
- Continuation lines in the definition must be indented (e.g. two spaces). Do not start continuation lines with additional `:` characters unless you intend to add a second definition for the same term.
- For multi-paragraph definitions, keep subsequent paragraphs indented to stay inside the same `<dd>`.
- For display math inside a definition, do not prefix every math line with `:`. Use exactly one `:` line to start the definition, then indent the `$$...$$` block normally. If each line of a `$$` block begins with `:`, math rendering can break.

Template:

```markdown
Claim (short sentence)
: First paragraph of the definition.
  Second line of the same paragraph (indented).

  $$
  Display math can be multiline.
  $$

  A second paragraph is ok if it stays indented.
```
