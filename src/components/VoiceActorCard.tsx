import React, { useId } from 'react';
import type { VoiceActor } from '../types';

interface VoiceActorCardProps {
  actor: VoiceActor;
}

const VoiceActorCard: React.FC<VoiceActorCardProps> = ({ actor }) => {
  const headingId = useId();
  const audioId = useId();
  const audioLabelId = useId();

  return (
    <article className="voice-actor-card" aria-labelledby={headingId}>
      <div className="voice-actor-card__header">
        <h2 id={headingId}>{actor.name}</h2>
        <p className="voice-actor-card__characters">
          {actor.characters.join(', ')}
        </p>
      </div>
      <p className="voice-actor-card__bio">{actor.biography}</p>
      <a
        href={actor.moreInfoUrl}
        className="voice-actor-card__link"
        target="_blank"
        rel="noreferrer"
      >
        Learn more about {actor.name}
      </a>
      <div className="voice-actor-card__audio">
        <span id={audioLabelId} className="voice-actor-card__audio-label">
          Sample clip
        </span>
        <audio
          id={audioId}
          aria-labelledby={audioLabelId}
          controls
          preload="none"
        >
          <source src={actor.sampleAudioUrl} type="audio/mpeg" />
          Your browser does not support the audio element.
        </audio>
      </div>
    </article>
  );
};

export default VoiceActorCard;
