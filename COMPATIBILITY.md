# LLM and agent-harness compatibility

This MagneticProxy skill pack is designed for Claude, Codex, GLM, DeepSeek, and other models or agent harnesses that can load Markdown instructions and local resources.

## Portable core

- Every workflow is defined in a standard `SKILL.md` with YAML frontmatter and Markdown instructions.
- References are Markdown files linked with relative paths.
- Helper scripts use ordinary Python 3 and do not import a model SDK.
- No workflow requires a model-specific tool name, prompt syntax, or proprietary memory feature.
- Cross-skill routing uses file-relative links. Harnesses without automatic skill discovery should load the specialized skill and `skills/magneticproxy/SKILL.md` together.

## Optional adapter

Files under `agents/openai.yaml` are optional Codex/OpenAI display metadata. Other harnesses can ignore them without losing any workflow, safety rule, product fact, or testable output.

## Portability rules

Preserve the full folder structure, including relative references and scripts. Give the runtime read access to Markdown and permission before it runs a helper script or uses live credentials. The skills ask before making network requests, running a scraper or browser, or changing a production schedule, and they remain limited to authorized targets regardless of the selected model.
