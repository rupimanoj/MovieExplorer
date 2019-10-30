import React from 'react';
import {Link, NavLink} from 'react-router-dom';
const Navbar = () => {
    return(
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <Link className="navbar-brand" to="/">
            Explore Movies
        </Link>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div className="navbar-nav">
            <NavLink className="nav-item nav-link" to="/explore">Explore</NavLink>
            <NavLink className="nav-item nav-link" to="/movies">Movies</NavLink>
            <NavLink className="nav-item nav-link" to="/shows">Shows</NavLink>
            <NavLink className="nav-item nav-link" to="/reviews">Reviews</NavLink>
          </div>
        </div>
      </nav>


    );
}



/*
classNameName Navbar extends Component {
    render() { 
        return (<nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="collapse navbar-collapse" id="navbarNavDropdown">
          <ul className="navbar-nav">
            <li className="nav-item active">
              <NavLink className="nav-link" to="/movies">Movies<NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/reviews">Reviews<NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/shows">Shows<NavLink>
            </li>
          </ul>
        </div>
      </nav>);

        
        return (<nav classNameName="navbar navbar-expand-lg navbar-light bg-light">
        <div classNameName="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div classNameName="navbar-nav">
            <NavLink classNameName="nav-item nav-link" to="#">Movies<NavLink>
            <NavLink classNameName="nav-item nav-link" to="#">Reviews<NavLink>
            <NavLink classNameName="nav-item nav-link" to="#">Shows<NavLink>
          </div>
        </div>
      </nav>  );
      
    }
}
 */
export default Navbar;