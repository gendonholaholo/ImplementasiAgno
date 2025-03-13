import React, { useState } from "react";
import axios from "axios";

const Home = () => {
  const [inputText, setInputText] = useState("");
  const [outputText, setOutputText] = useState("");

  const handleSubmit = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/process-agno", {
        input_text: inputText,
      });
      setOutputText(response.data.output);
    } catch (error) {
      console.error("Error processing Agno:", error);
    }
  };

  return (
    <div style={{ padding: "20px", textAlign: "center" }}>
      <h1>Agno Text Processor</h1>
      <input
        type="text"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter text..."
      />
      <button onClick={handleSubmit}>Process</button>
      {outputText && (
        <div>
          <h3>Processed Output:</h3>
          <p>{outputText}</p>
        </div>
      )}
    </div>
  );
};

export default Home;
