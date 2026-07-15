from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.proposalAgent.models.db_models import create_tables
from appRouter import router

print(
    "Hello from main.py!", flush=True
)  # Debug statement to confirm the file is being executed


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Initializing database...", flush=True)
    create_tables()

    yield

    print("Shutting down...", flush=True)


app = FastAPI(lifespan=lifespan)
app.include_router(router)


# {
#   "title": "AI-Powered Customer Support Chatbot for E-Commerce Platform",
#   "description": "Build an AI-powered customer support chatbot that can answer frequently asked customer questions, assist with order tracking, handle product recommendations, and escalate complex issues to human support agents. The chatbot should integrate with the company's Shopify store, CRM, and Zendesk support system. The goal is to reduce customer support workload while improving response times and customer satisfaction.",
#   "budget": 75000.0,
#   "call_notes": "Discovery Call Summary:\n\nClient: TrendKart E-Commerce Pvt. Ltd.\nAttendees: Sarah Johnson (Head of Customer Experience), Michael Lee (CTO), David Wilson (Support Operations Manager)\n\nCurrent Challenges:\n- Customer support team receives over 2,500 tickets per week.\n- Approximately 65% of tickets are repetitive questions related to shipping status, return policy, refund requests, and product availability.\n- Average first response time is 7 hours, which negatively impacts customer satisfaction.\n- During seasonal sales, ticket volume nearly doubles, requiring temporary staffing.\n\nBusiness Goals:\n- Automate responses for common customer queries.\n- Reduce support ticket volume by at least 50%.\n- Improve average response time to under 30 seconds.\n- Provide personalized product recommendations using purchase history.\n- Support English initially, with plans for Spanish and French in Phase 2.\n\nTechnical Requirements:\n- Integrate with Shopify APIs.\n- Integrate with Zendesk for ticket creation and escalation.\n- Connect with Salesforce CRM to retrieve customer information.\n- Support both website chat widget and mobile application.\n- Maintain conversation history for returning customers.\n\nNon-functional Requirements:\n- Response time under 2 seconds.\n- GDPR compliance.\n- Role-based access for administrators.\n- Analytics dashboard showing conversation metrics, resolution rates, and customer satisfaction.\n\nExpected Timeline:\n- MVP in 10 weeks.\n- Production launch in 14 weeks.\n\nSuccess Metrics:\n- 50% reduction in support tickets.\n- Customer satisfaction score above 90%.\n- 24/7 automated support availability.\n- Less than 10% escalation rate for automated conversations.",
#   "prospect_url": "https://www.trendkart-demo.com",
#   "additional_context": "The client previously evaluated Intercom Fin AI and Zendesk AI but found them expensive and difficult to customize. They are looking for a custom AI solution built using modern LLMs with retrieval-augmented generation (RAG). The solution should use their internal product catalog, FAQ documentation, return policy, shipping policy, and knowledge base to answer customer questions accurately. They are also interested in future enhancements such as voice support, AI-generated support ticket summaries, sentiment analysis, and multilingual capabilities. The proposal should include an executive summary, business objectives, proposed solution architecture, implementation phases, technology stack, timeline, estimated effort, pricing assumptions, risks, and next steps."
# }
