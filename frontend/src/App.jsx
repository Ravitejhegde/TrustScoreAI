import { useState } from "react";

import axios from "axios";

function App() {

  const [file, setFile] = useState(null);

  const [message, setMessage] = useState("");

  function chooseImage(event) {

    setFile(

      event.target.files[0]

    );

  }

  async function uploadImage() {

    if (!file) {

      alert("Choose image first");

      return;

    }

    const formData = new FormData();

    formData.append(

      "image",

      file

    );

    const response = await axios.post(

      "http://127.0.0.1:8000/upload",

      formData

    );

    setMessage(

      response.data.message

    );

  }

  return (

    <div

      style={{

        height:"100vh",

        display:"flex",

        flexDirection:"column",

        justifyContent:"center",

        alignItems:"center"

      }}

    >

      <h1>

        TrustScoreAI

      </h1>

      <input

        type="file"

        onChange={chooseImage}

      />

      <button

        onClick={uploadImage}

      >

        Upload

      </button>

      <h3>

        {message}

      </h3>

    </div>

  )

}

export default App;