function CircularScore({ score, risk }) {

  if (score === undefined) {

    return null;

  }

  return (

    <div className="circleContainer">

      <div className="circle">

        <h1>

          {score}

        </h1>

        <p>

          /100

        </p>

      </div>

      <h2>

        {risk}

      </h2>

    </div>

  );

}

export default CircularScore;