from .rag_pipeline import generate_answer
import openai

def agentic_task(question):
    # Example: AI can fetch docs, summarize, and suggest next steps
    answer = generate_answer(question)
    followup_prompt = f"Based on the previous answer, suggest next actionable steps:\n{answer}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=followup_prompt,
        temperature=0.3,
        max_tokens=150
    )
    return {
        "answer": answer,
        "next_steps": response['choices'][0]['text'].strip()
    }
