from speechbrain.pretrained import VAD

VAD = VAD.from_hparams(source="speechbrain/vad-crdnn-libriparty", savedir="pretrained_models/vad-crdnn-libriparty")

# 1- Let's compute frame-level posteriors first
audio_file = '/data1/antinomysu/sg_data/三国演义：第1集 桃园三结义.wav'
prob_chunks = VAD.get_speech_prob_file(audio_file)

# 2- Let's apply a threshold on top of the posteriors
prob_th = VAD.apply_threshold(prob_chunks).float()

# 3- Let's now derive the candidate speech segments
boundaries = VAD.get_boundaries(prob_th)

# 4- Apply energy VAD within each candidate speech segment (optional)

boundaries = VAD.energy_VAD(audio_file,boundaries)

# 5- Merge segments that are too close
boundaries = VAD.merge_close_segments(boundaries, close_th=1.0)

# 6- Remove segments that are too short
boundaries = VAD.remove_short_segments(boundaries, len_th=0.250)

# 7- Double-check speech segments (optional).
boundaries = VAD.double_check_speech_segments(boundaries, audio_file,  speech_th=0.5)

VAD.save_boundaries(boundaries)
# VAD.get_segments(boundaries,audio_file)