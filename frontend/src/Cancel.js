import React from "react";

function Cancel() {
  return (
    <div className="app">
      <div className="card">
        <h1 style={{ marginBottom: "20px" }}>❌ Payment Cancelled</h1>

        <p style={{ color: "#444", fontSize: "17px", marginBottom: "25px", lineHeight: "1.6" }}>
          Your payment was not completed. If this was a mistake, you can try again at any time.
        </p>

        <p style={{ color: "#444", fontSize: "16px", marginBottom: "20px", lineHeight: "1.6" }}>
          No charge has been made, and your writing style analysis has not been started.
        </p>

        <p style={{ color: "#667eea", fontWeight: "bold", fontSize: "16px", marginBottom: "40px" }}>
          If you need help or have questions, feel free to contact support.
        </p>

        <a href="/" style={{
          textDecoration: "none",
          display: "inline-block",
          padding: "12px 24px",
          backgroundColor: "#667eea",
          color: "#fff",
          borderRadius: "8px",
          fontSize: "16px",
          transition: "background-color 0.3s"
        }}>
          ⬅ Back to Home
        </a>
      </div>
    </div>
  );
}

export default Cancel;
