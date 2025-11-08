import React from 'react';
import VoiceActorList from './components/VoiceActorList';
import voiceActorData from './data/voiceActors.json';
import type { VoiceActor } from './types';

const voiceActors: VoiceActor[] = voiceActorData;

const App: React.FC = () => {
  return (
    <div className="app">
      <header className="app__header">
        <h1>Regular Show Voice Actor Explorer</h1>
        <p className="app__tagline">
          Discover the talented voices behind Mordecai, Rigby, and the rest of the park crew.
        </p>
      </header>
      <main>
        <VoiceActorList actors={voiceActors} />
      </main>
      <footer className="app__footer">
        <small>
          Audio clips are provided for educational preview purposes only.
        </small>
      </footer>
    </div>
  );
};

export default App;
