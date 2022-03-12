import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Navbar from './components/layout/Navbar';
import Login from './views/auth/Login';
import Logout from './views/auth/Logout'; 
import Register from './views/auth/Register'; 
import Dashboard from './views/auth/Dashboard'; 
import Cliente from './views/auth/Cliente'; 
import Tarifas from './views/auth/Tarifas'; 

const App = () => {
  return (
    <div className='App'>
      <Router>
        <Navbar />
        <Switch>
          <Route path='/login' component={Login} exact />
          <Route path='/register' component={Register} exact />
          <Route path='/logout' component={Logout} exact />
          <Route path='/dashboard' component={Dashboard} exact />
          <Route path='/cliente' component={Cliente} exact />
          <Route path='/tarifas' component={Tarifas} exact />
        </Switch>
      </Router>
    </div>
  );
};

export default App;