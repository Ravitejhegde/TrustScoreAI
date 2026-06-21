import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {

  const [image, setImage] = useState(null);

  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);

  function handleImage(event) {

    const selectedFile = event.target.files[0];

    console.log(selectedFile);

    setImage(selectedFile);

  }

  async function analyzeImage() {

    console.log(image);

    if (!image) {

      alert("Please select an image");

      return;

    }

    setLoading(true);

    try {

      const formData = new FormData();

      formData.append(

        "image",

        image

      );

      const response = await axios.post(

        "http://127.0.0.1:8000/analyze",

        formData

      );

      console.log(response.data);

      setResult(

        response.data

      );

    }

    catch (error) {

      console.log(error);

      alert(

        "Analysis failed"

      );

    }

    finally {

      setLoading(false);

    }

  }

  async function downloadPDF() {

    if (!image) {

      alert("Please select image");

      return;

    }

    try {

      const formData = new FormData();

      formData.append(

        "image",

        image

      );

      const response = await axios.post(

        "http://127.0.0.1:8000/download-report",

        formData,

        {

          responseType: "blob"

        }

      );

      const url = window.URL.createObjectURL(

        new Blob(

          [response.data]

        )

      );

      const link = document.createElement(

        "a"

      );

      link.href = url;

      link.download = "trustscore_report.pdf";

      document.body.appendChild(

        link

      );

      link.click();

      link.remove();

    }

    catch (error) {

      console.log(error);

      alert(

        "PDF download failed"

      );

    }

  }

  return (

    <div className="container">

      <h1>

        TrustScoreAI

      </h1>

      <p>

        Analyze images and estimate whether they were AI-generated

      </p>

      <input

        type="file"

        accept=".jpg,.jpeg,.png,.webp"

        onChange={handleImage}

      />

      <br />

      <br />

      <button

        onClick={analyzeImage}

      >

        Analyze Image

      </button>

      <button

        onClick={downloadPDF}

      >

        Download PDF

      </button>

      {loading && (

        <h3>

          Analyzing...

        </h3>

      )}

      {result && (

        <div>

          <h2>

            {result.trust_score}/100

          </h2>

          <h3>

            {result.risk_level}

          </h3>

          <h3>

            Reasons

          </h3>

          <ul>

            {

              result.reasons.map(

                (item,index)=>(

                  <li key={index}>

                    {item}

                  </li>

                )

              )

            }

          </ul>

          <h3>

            Indicators

          </h3>

          <ul>

            {

              result.indicators.map(

                (item,index)=>(

                  <li key={index}>

                    {item}

                  </li>

                )

              )

            }

          </ul>

        </div>

      )}

    </div>

  );

}

export default App;