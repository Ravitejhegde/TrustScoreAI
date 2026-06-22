import CircularScore from "./CircularScore";

function ResultsCard({ result }) {

  if (!result) {

    return null;

  }

  return (

    <div className="results">

      <CircularScore

        score={result.trust_score}

        risk={result.risk_level}

      />

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

  );

}

export default ResultsCard;