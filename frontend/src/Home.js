import React, { useEffect, useState } from 'react';
import { loadStripe } from "@stripe/stripe-js";



const stripePromise = loadStripe(process.env.REACT_APP_STRIPE_API_KEY); // your public key
const BACKEND_URL = process.env.REACT_APP_BACKEND_URL; // your backend URL

function Home() {
  const [username1, setUsername1] = useState("");
  const [username2, setUsername2] = useState("");
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const activateBackend = async () => {
      try {
        const response = await fetch(`${BACKEND_URL}/activate-backend`, {
          method: "GET",
          headers: { "Content-Type": "application/json" }
        });
      }
      catch (error) {
        console.error("Error activating backend:", error);
      }
    };
    activateBackend();
  }, []);

  const handlePayment = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      // 1. Check usernames exist
      const checkRes = await fetch(`${BACKEND_URL}/check-usernames`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username1, username2 })
      });

      const checkData = await checkRes.json();

      if (!checkRes.ok || !checkData.valid) {
        setError("❌ One or both Twitter usernames do not exist.");
        setLoading(false);
        return;
      }

      const stripe = await stripePromise;

      // 2. Create Stripe checkout session
      const sessionRes = await fetch(`${BACKEND_URL}/create-checkout-session`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          email,
          current_user: username1,
          target_user: username2
        })
      });

      const sessionData = await sessionRes.json();
      if (sessionRes.ok && sessionData.id) {
        await stripe.redirectToCheckout({ sessionId: sessionData.id });
      } else {
        setError("❌ Failed to create checkout session.");
        setLoading(false);
      }

    } catch (err) {
      console.error("Payment error:", err);
      setError("Something went wrong. Please try again.");
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="card">
        <h1 style={{ marginBottom: "20px" }}>Match Your Twitter Writing Style</h1>

        <p style={{ color: "#555", fontSize: "16px", marginBottom: "30px", lineHeight: "1.6" }}>
          Want to write tweets like your favorite influencer or friend?
          This tool analyzes the writing style of two Twitter accounts — yours and theirs —
          and gives you a personalized breakdown on how to tweet more like them. 🔍✨
        </p>

        <ul style={{ textAlign: "left", marginBottom: "30px", color: "#444", lineHeight: "1.8", paddingLeft: "20px", listStyleType: "none"  }}>
          <li>1️⃣ Enter your Twitter username</li>
          <li>2️⃣ Enter the username of the person you'd like to emulate</li>
          <li>3️⃣ Enter your email and pay $9 via Stripe</li>
          <li>4️⃣ Get a detailed comparison and improvement tips directly to your inbox</li>
        </ul>

        <p style={{
          fontWeight: "bold",
          color: "#667eea",
          fontSize: "17px",
          marginBottom: "40px"
        }}>
          Just $9 for a personalized writing style analysis and transformation guide.
        </p>

        <form onSubmit={handlePayment} style={{ display: "flex", flexDirection: "column", gap: "20px" }}>
          <input
            type="text"
            placeholder="Your Twitter username"
            value={username1}
            onChange={(e) => setUsername1(e.target.value)}
            required
          />
          <input
            type="text"
            placeholder="Their Twitter username"
            value={username2}
            onChange={(e) => setUsername2(e.target.value)}
            required
          />
          <input
            type="email"
            placeholder="Your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <button type="submit" disabled={loading}>
            {loading ? "Checking..." : "Pay $9 with Stripe"}
          </button>
        </form>

        {error && <p style={{ color: "red", marginTop: "25px" }}>{error}</p>}

        <div className="result" style={{ marginTop: "50px", textAlign: "left" }}>
          <h2 style={{ color: "#333", marginBottom: "15px" }}>What you’ll receive:</h2>
          <ul style={{ paddingLeft: "20px", color: "#444", lineHeight: "1.8", listStyleType: "none"  }}>
            <li>✅ Key writing traits of both accounts</li>
            <li>✅ A comparison of tone, vocabulary, and structure</li>
            <li>✅ Personalized writing tips to match their style</li>
            <li>✅ Delivery within minutes straight to your inbox</li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Home;
