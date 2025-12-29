# Nexus-Guardian 🛡️

**Nexus-Guardian** is an advanced, autonomous Multi-Agent DevSecOps system designed to self-heal code repositories. Inspired by the latest advancements in Generative AI agents (like *GenAI_Agents* and *strix*), Nexus-Guardian employs a "Red Team / Blue Team" architecture to proactively identify and fix security vulnerabilities in real-time.

## 🚀 Key Features

*   **Dual-Agent Architecture**:
    *   🔴 **Red Agent**: Scans codebase for vulnerabilities, logic flaws, and security risks (inspired by *strix*).
    *   🔵 **Blue Agent**: Automatically generates secure patches and refactors code to resolve issues found by the Red Agent.
*   **Automated Documentation**: Generates architectural decision records (ADR) for every fix applied.
*   **Extensible Design**: Built to support Model Context Protocol (MCP) for future tool integrations.

## 🏗️ Architecture

The system operates on a loop:
1.  **Scan Phase**: Red Agent analyzes the target directory.
2.  **Report Phase**: Vulnerabilities are prioritized based on severity.
3.  **Heal Phase**: Blue Agent generates patches.
4.  **Verify Phase**: (Optional) Red Agent re-scans to verify the fix.

## 🛠️ Installation

```bash
git clone https://github.com/arturwyroslak/Nexus-Guardian.git
cd Nexus-Guardian
pip install -r requirements.txt
```

## 💻 Usage

Run the autonomous guardian on your current project:

```bash
python main.py --path ./my-project --mode auto-fix
```

## 🔮 Future Roadmap

*   Integration with live CI/CD pipelines (GitHub Actions).
*   MCP Server implementation to allow IDEs (Cursor/VS Code) to talk directly to Nexus-Guardian.
*   RAG-enhanced context awareness using a vector database.
