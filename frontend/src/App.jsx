import { useState } from "react";

import axios from "axios";

import "./App.css";

import Header from "./components/Header";

import UploadBox from "./components/UploadBox";

import ImagePreview from "./components/ImagePreview";

import ResultsCard from "./components/ResultsCard";

import Disclaimer from "./components/Disclaimer";

import History from "./components/History";

function App() {

  const [image, setImage] = useState(null);

  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);

  const [history,setHistory] = useState([]);


  function handleImage(event) {

    const selectedFile = event.target.files[0];

    setImage(selectedFile);

  }


  async function analyzeImage() {

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

      setResult(

        response.data

      );

      setHistory(

previous => [

{

name:image.name,

score:response.data.trust_score,

risk:response.data.risk_level,

time:new Date().toLocaleTimeString()

},

...previous

]

);

<History

history={history}

/>

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

      alert(

        "Please select image"

      );

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

      link.download =

        "trustscore_report.pdf";

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

      <Header />

      <UploadBox

        handleImage={handleImage}

      />

      <ImagePreview

        image={image}

      />

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

      <ResultsCard

        result={result}

      />

      <Disclaimer />

    </div>

  );

}


export default App;