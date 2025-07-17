import React, { useState } from "react";
import { createRoot } from "react-dom/client";
import axios from "axios";

function App() {
  const [url, setUrl] = useState("");
  const [format, setFormat] = useState("mp4");
  const [loading, setLoading] = useState(false);

  const handleDownload = async () => {
    setLoading(true);
    try {
      const response = await axios.post("http:
        url,
        format,
      }, { responseType: 'blob' });

      const blob = new Blob([response.data]);
      const downloadUrl = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = downloadUrl;
      a.download = \`download.\${format}\`;
      a.click();
    } catch (err) {
      alert("Download failed");
    }
    setLoading(false);
  };

  return (
    <div>
      <h1>YouTube Downloader</h1>
      <input value={url} onChange={e => setUrl(e.target.value)} placeholder="YouTube URL" />
      <select onChange={e => setFormat(e.target.value)} value={format}>
        <option value="mp4">MP4</option>
        <option value="mp3">MP3</option>
      </select>
      <button onClick={handleDownload} disabled={loading}>
        {loading ? "Downloading..." : "Download"}
      </button>
    </div>
  );
}

const root = createRoot(document.getElementById("root"));
root.render(<App />);