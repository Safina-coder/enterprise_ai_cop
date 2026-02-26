import React, { useState } from "react";

export default function ChatBox() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const askQuestion = async () => {
    const res = await fetch("http://localhost:8000/agentic", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })
    });
    const data = await res.json();
    setAnswer(`Answer: ${data.answer}\nNext Steps: ${data.next_steps}`);
  };

  return (
    <div>
      <textarea value={question} onChange={(e) => setQuestion(e.target.value)} />
      <button onClick={askQuestion}>Ask AI</button>
      <pre>{answer}</pre>
    </div>
  );
}
