import React from "react";

import background from "./assets/background.png";

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar/Navbar";

import Footer from "./components/Footer/Footer";

import Home from "./pages/Home";

import History from "./pages/History";

import About from "./pages/About";

import NotFound from "./pages/NotFound";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <main
        style={{
          backgroundImage: `url(${background})`,
          backgroundSize: "cover",
          backgroundPosition: "center",
          backgroundRepeat: "no-repeat",
          backgroundAttachment: "fixed",
          minHeight: "85vh"
        }}
      >
        <Routes>

          <Route path="/" element={<Home />} />

          <Route path="/history" element={<History />} />

          <Route path="/about" element={<About />} />

          <Route path="*" element={<NotFound />} />

        </Routes>
      </main>

      <Footer />
    </BrowserRouter>
  );
}

export default App;