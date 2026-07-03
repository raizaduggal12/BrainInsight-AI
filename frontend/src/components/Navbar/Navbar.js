import { Link } from "react-router-dom";
import logo from "../../assets/caduceus.png";

import "./Navbar.css";

function Navbar() {

    return (

        <nav className="navbar">

            <div className="logo" style={{fontSize:"25px"}}>
                <img
                    src={logo}
                    alt="BrainInsight Logo"
                    className="logo-img"
                    style={{ height: "40px" }}
                />
                <span>BrainInsight <span style={{ color: "#2E8BFF" }}>AI</span></span>
            </div>

            <ul className="nav-links">

                <li>

                    <Link to="/" style={{fontSize:"25px"}}>Home</Link>

                </li>

                <li>

                    <Link to="/history" style={{fontSize:"25px"}}>History</Link>

                </li>

                <li>

                    <Link to="/about" style={{fontSize:"25px"}}>About</Link>

                </li>

            </ul>

        </nav>

    );

}

export default Navbar;