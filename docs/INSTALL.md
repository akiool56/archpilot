# Install

Project-level:

```text
your-project/.claude/skills/archpilot/
```

User-level:

```text
~/.claude/skills/archpilot/
```

Validate:

```bash
python scripts/validate_skill.py
```

Expected:

```text
OK: skill package structure is valid.
```


## Important structure rule

最终结构必须是：

```text
~/.claude/skills/archpilot/SKILL.md
~/.claude/skills/archpilot/references/
~/.claude/skills/archpilot/templates/
```

`SKILL.md` 必须直接位于 `archpilot` 目录下，不要多套一层版本目录。
