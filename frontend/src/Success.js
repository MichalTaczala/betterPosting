import React from "react";

function Success() {
  return (
    <div className="app">
      <div className="card">
        <h1 style={{ marginBottom: "20px" }}>🎉 Payment Successful!</h1>

        <p style={{ color: "#444", fontSize: "17px", marginBottom: "25px", lineHeight: "1.6" }}>
          Thank you for your purchase. We've received your payment and our system is now analyzing the writing styles of both Twitter accounts.
        </p>

        <p style={{ color: "#444", fontSize: "16px", marginBottom: "20px", lineHeight: "1.6" }}>
          You should receive your personalized comparison and style-matching tips in your email inbox within the next few minutes. 📩
        </p>

        <p style={{ color: "#667eea", fontWeight: "bold", fontSize: "16px", marginBottom: "40px" }}>
          If you don't see the email, make sure to check your spam or promotions folder.
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

export default Success;
