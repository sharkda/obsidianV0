
**1. Session START is passive — Claude won't actually do it**

The protocol says "Search vault" but Claude Code won't run it automatically unless you explicitly trigger it. Add this at the top:

markdown

```markdown
## Activation
At the start of EVERY session, immediately run the Session START protocol 
without waiting to be asked.
```