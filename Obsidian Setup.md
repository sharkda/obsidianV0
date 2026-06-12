
## local Vault 
I have moved Obsidian to local, the cloud storage threading model will stop the mcp gateway run and nothing got written. unless moved to local.
so there is no synch, unless I git the vault

### git the vault and synch it 

**One-time setup** (in your vault root):

bash

```bash
cd /path/to/your/vault
git init
# add the .gitignore file from before, then:
git add .
git commit -m "Initial vault snapshot"

# create an empty PRIVATE repo on GitHub first, then:
'git@github.com:sharkda/obsidianV0.git'
git remote add origin git@github.com:sharkda/obsidianV0.git
##git remote add origin git@github.com:yourname/obsidian-vault.git
git branch -M main
git push -u origin main
```

**Recurring cycle** (whenever you want to back up):

bash

```bash
git add -A
git commit -m "vault backup $(date +%F)"
git push
```

### make it run handsfree


the vault path is 
**~/Library/Mobile Documents/com~apple~CloudDocs/obsidianV0

claude mcp add obsidian -- npx -y obsidian-mcp "Library/Mobile Documents/com~apple~CloudDocs/obsidianV0"

"OBSIDIAN_API_KEY": "cbf237257e989f195dd9a64e0126accc6c3f1697279a0225630789686d0ef11e"

claude mcp add obsidian -e OBSIDIAN_API_KEY="cbf237257e989f195dd9a64e0126accc6c3f1697279a0225630789686d0ef11e" -- npx -y mcp-obsidian

```bash
curl -s http://localhost:27123 -H "Authorization: Bearer YOUR_API_KEY_HERE"
```

curl -s http://localhost:27123 -H "Authorization: Bearer cbf237257e989f195dd9a64e0126accc6c3f1697279a0225630789686d0ef11e"

 When you're ready to continue, the fix is:                                         

  claude mcp remove "obsidian" -s local                                              

···
claude mcp add obsidian -s local -e OBSIDIAN_API_KEY=cbf237257e989f195dd9a64e0126accc6c3f1697279a0225630789686d0ef11e -- npx -y mcp-obsidian "~/Library/Mobile Documents/com~apple~CloudDocs/obsidianV0"
···




"mcpServers": {

        "obsidian": {

          "type": "stdio",

          "command": "npx",

          "args": [

            "-y",

            "mcp-obsidian",

            "~/Library/Mobile Documents/com~apple~CloudDocs/obsidianV0"

          ],

          "env": {

            "OBSIDIAN_API_KEY": "cbf237257e989f195dd9a64e0126accc6c3f1697279a0225630789686d0ef11e"

          }

        }

      },

was between 

"mcpContextUris": [],

      "enabledMcpjsonServers": [],
      
      
      
      
      Create a note in my Obsidian vault called "test-claude-memory.md" with the content "Claude Code MCP connection verified on this Old M0"