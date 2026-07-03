import "./HistoryTable.css";

function HistoryTable({ history = [] }) {
  return (
    <table className="history-table">
      <thead>
        <tr>
          <th>Patient ID</th>

          <th>Prediction</th>

          <th>Confidence</th>

          <th>Severity</th>

          <th>Date</th>
        </tr>
      </thead>

      <tbody>
        {history.length > 0 ? (
          history.map((item, index) => (
            <tr key={index}>
              <td>{item.patient_id}</td>

              <td>
                {item.prediction.charAt(0).toUpperCase() +
                  item.prediction.slice(1)}
              </td>

              <td>{item.confidence}%</td>

              <td>{item.severity}</td>

              <td>{item.prediction_date}</td>
            </tr>
          ))
        ) : (
          <tr>
            <td colSpan="5" style={{ textAlign: "center" }}>
              No prediction history found.
            </td>
          </tr>
        )}
      </tbody>
    </table>
  );
}

export default HistoryTable;
