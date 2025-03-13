import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

export const processAgno = async (inputText) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/process-agno`, {
      input_text: inputText,
    });
    return response.data.output;
  } catch (error) {
    console.error("API Error:", error);
    return null;
  }
};
