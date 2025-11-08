import { render, screen, within } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import VoiceActorList from '../components/VoiceActorList';
import voiceActors from '../data/voiceActors.json';

describe('VoiceActorList', () => {
  it('renders all Regular Show voice actors from the data file', () => {
    render(<VoiceActorList actors={voiceActors} />);

    voiceActors.forEach((actor) => {
      expect(screen.getByRole('heading', { name: actor.name })).toBeInTheDocument();
      expect(screen.getByText(actor.biography)).toBeInTheDocument();
    });
  });

  it('associates audio controls with accessible labels and allows playback interaction', async () => {
    const user = userEvent.setup();
    render(<VoiceActorList actors={voiceActors} />);

    const firstActor = voiceActors[0];
    const card = screen.getByRole('article', { name: firstActor.name });

    const sampleLabel = within(card).getByText(/sample clip/i);
    const audio = within(card).getByLabelText(/sample clip/i);

    expect(audio).toHaveAttribute('controls');
    expect(audio).toHaveAttribute('preload', 'none');

    await user.click(sampleLabel);
    expect(audio).toBeInstanceOf(HTMLAudioElement);
  });
});
