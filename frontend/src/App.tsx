import React, { FC } from 'react';
import Newsletter from './views/newsletter';

import 'bootstrap/dist/css/bootstrap.min.css';

const App: FC = () => {
  return (
    <div className="container" style={{ marginTop: 100 }}>
      <Newsletter />
    </div>
  );
};

export default App;
