import { useState } from "react";
import bgImage from "./assets/bg.png"; 

function App() {
  const [name, setName] = useState("");
  const [address, setAddress] = useState("");
  const [issue, setIssue] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!name || !address || !issue) {
      alert("Please fill all fields");
      return;
    }

    const response = await fetch("http://127.0.0.1:5000/generate-rti", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name, address, issue }),
    });

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "rti.pdf";
    a.click();
  };

  return (
    <div
      className="min-h-screen flex items-center justify-center bg-cover bg-center relative"
      style={{ backgroundImage: `url(${bgImage})` }}
    >
      <div className="absolute inset-0 bg-black/40"></div>


      <div className="relative bg-white/10 backdrop-blur-xl p-8 rounded-2xl shadow-2xl w-[350px] border border-white/30">
        
        <h2 className="text-2xl font-bold text-center text-white mb-6">
         RTI Generator
        </h2>

        <form onSubmit={handleSubmit} className="flex flex-col gap-4">

          <input
            className="p-2 rounded-md bg-white/70 outline-none"
            placeholder="Enter your name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />

          <input
            className="p-2 rounded-md bg-white/70 outline-none"
            placeholder="Enter your address"
            value={address}
            onChange={(e) => setAddress(e.target.value)}
          />

          <textarea
            className="p-2 rounded-md bg-white/70 outline-none h-24 resize-none"
            placeholder="Describe your issue (any language)"
            value={issue}
            onChange={(e) => setIssue(e.target.value)}
          />

          <button
            className="bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition"
            type="submit"
          >
            Generate RTI PDF
          </button>

        </form>
      </div>
    </div>
  );
}

export default App;