import { useState, useEffect } from 'react'


// const API_URL = import.meta.env.VITE_API_URL

function App() {
  const [message, setMessage] = useState("")

  useEffect(() => {
    fetch(`/api/users`)
      .then(res => res.json())
      .then(data => setMessage(data.message));
  }, []);

  return <h1>{message}</h1>;
}

export default App
