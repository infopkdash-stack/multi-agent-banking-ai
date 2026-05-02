# 🏦 Multi-Agent Banking AI System (LangGraph + RAG + LLM)

## 💡 Business Problem

Banking production support teams handle a high volume of operational incidents such as:

* Payment transaction failures
* General Ledger (GL) mismatches
* Batch processing delays
* Trade finance authorization issues

These issues are typically resolved **manually**, leading to:

* ⏱️ Increased MTTR (Mean Time to Resolution)
* 💰 High operational costs
* ⚠️ SLA breaches and business impact

---

## 🚀 Solution

This project implements a **production-style Multi-Agent AI System** that automates L1/L2 banking support workflows using:

* 🤖 **LLMs (Large Language Models)**
* 🔄 **LangGraph (Agent Orchestration)**
* 🔍 **RAG (Retrieval-Augmented Generation)**

### 🔧 Key Capabilities

* Intelligent issue diagnosis (module identification)
* Log-level analysis with technical insights
* Context-aware resolution using historical incidents
* Actionable, step-by-step recommendations

👉 Designed for **AI-assisted banking operations and incident management**

---

## 🧠 System Architecture

```
User Query
   ↓
Diagnostic Agent  → Identifies module + confidence
   ↓
Log Analysis Agent → Detects technical/log-level issues
   ↓
RAG Layer (FAISS) → Retrieves similar past incidents
   ↓
Resolution Agent → Generates root cause + fix steps
   ↓
Final Response (UI)
```

---

## 🤖 Multi-Agent Design

### 🔹 Diagnostic Agent

* Classifies issue into banking modules:

  * Payments
  * General Ledger
  * Trade Finance
* Adds **confidence scoring**
* Combines rule-based + LLM reasoning

---

### 🔹 Log Analysis Agent

* Identifies:

  * Timeout issues
  * Transaction failures
  * Batch processing errors
* Suggests logs and checks to investigate

---

### 🔹 Resolution Agent

* Determines **root cause**
* Provides **step-by-step resolution**
* Uses:

  * Log analysis
  * RAG context
* Suggests **preventive measures**

---

## 🧠 RAG Implementation (Core Strength)

* Historical incidents stored in **FAISS vector database**
* Semantic similarity search retrieves relevant cases
* Context injected into LLM for better responses

### ✅ Benefits:

* Reduced hallucination
* Domain-aware responses
* Context-driven decision making

---

## 🧪 Example Output

### 🔹 Input

```
Payment transaction stuck in processing
```

### 🔹 Output

```
Module: Payments
Confidence: High

Log Insight:
Possible timeout or payment gateway delay

Root Cause:
Payment gateway timeout due to delayed response

Resolution:
1. Retry the transaction
2. Check payment gateway connectivity
3. Validate timeout configuration

Preventive Measures:
- Increase timeout threshold
- Monitor gateway latency
```

---

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **LangGraph**
* **OpenAI / LLM APIs**
* **FAISS (Vector Database)**
* **Streamlit (UI)**
* **Docker (Deployment-ready)**

---

## 📂 Project Structure

```
multi-agent-banking-ai/
│── app/
│   ├── agents/
│   │   ├── diagnostic_agent.py
│   │   ├── log_agent.py
│   │   ├── resolution_agent.py
│   ├── graph.py
│   ├── rag.py
│   ├── config.py
│── ui/
│   ├── streamlit_app.py
│── data/
│   ├── incidents.json
│── screenshots/
│── requirements.txt
│── Dockerfile
│── README.md
```

---

## 📸 UI Preview

### 🔹 Input

![Input](screenshots/input.png)

### 🔹 Output

![Output](screenshots/output.png)

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/infopkdash-stack/multi-agent-banking-ai.git
cd multi-agent-banking-ai
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Add API Key

Create `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 4. Run Application

```bash
streamlit run ui/streamlit_app.py
```

---

## 🐳 Docker Setup

### Build

```bash
docker build -t banking-ai .
```

### Run

```bash
docker run -p 8501:8501 banking-ai
```

---

## ☁️ Deployment Options

* Streamlit Cloud (quick demo)
* AWS EC2 / GCP Cloud Run (production-style)
* Docker-based deployment

---

## 🎯 Use Cases

* Banking production support automation
* Incident diagnosis and resolution
* AI-assisted operations
* Decision support systems

---

## 📌 Future Enhancements

* Real-time log ingestion
* Pinecone / cloud vector DB integration
* Authentication & role-based access
* API deployment using FastAPI

---

## 👤 Author

**Prasanta Kumar Dash**
AI + Banking Systems | LLM | GenAI | Production Support Automation
