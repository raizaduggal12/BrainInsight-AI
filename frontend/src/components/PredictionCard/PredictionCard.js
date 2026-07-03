import "./PredictionCard.css";

function PredictionCard({ result }) {
  if (!result) return null;

  return (
    <div className="prediction-card">
      <h2>Prediction Result</h2>

      <p>
          Prediction :
          {" "}
          {result.prediction.prediction.charAt(0).toUpperCase() + result.prediction.prediction.slice(1)}
      </p>

      <p>
        <strong>Confidence : </strong>
        {result.prediction.confidence}%
      </p>
    </div>
  );
}

export default PredictionCard;
