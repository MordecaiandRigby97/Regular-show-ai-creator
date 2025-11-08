import React from 'react';
import VoiceActorCard from './VoiceActorCard';
import type { VoiceActor } from '../types';

interface VoiceActorListProps {
  actors: VoiceActor[];
}

const VoiceActorList: React.FC<VoiceActorListProps> = ({ actors }) => {
  return (
    <section aria-label="Regular Show voice actors" className="voice-actor-list">
      {actors.map((actor) => (
        <VoiceActorCard key={actor.name} actor={actor} />
      ))}
    </section>
  );
};

export default VoiceActorList;
