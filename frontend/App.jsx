import { useState } from "react"

function App() {
  const [url, setUrl] = useState("")
  const [format, setFormat] = useState("mp3")
  const [loading, setLoading] = useState(false)

  const handleDownload = async () => {
    setLoading(true)
    const res = await fetch("/api/download", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ url, format }),
    })
    if (res.ok) {
      const blob = await res.blob()
      const a = document.createElement("a")
      a.href = URL.createObjectURL(blob)
      a.download = "video." + format
      a.click()
    }
    setLoading(false)
  }

  return (
    <div style={{ padding: 40 }}>
      <h1>YouTube Downloader</h1>
      <input value={url} onChange={e => setUrl(e.target.value)} placeholder="YouTube URL" />
      <select value={format} onChange={e => setFormat(e.target.value)}>
        <option value="mp3">MP3</option>
        <option value="mp4">MP4</option>
      </select>
      <button onClick={handleDownload} disabled={loading}>
        {loading ? "Downloading..." : "Download"}
      </button>
    </div>
  )
}

export default App