const SAVE_KEY = 'siempre_listo_save';

const defaultSave = () => ({
  version: 1,
  playerName: 'Scouter',
  completedTopics: [],
  badges: [],
  quizScores: {},
  totalScore: 0,
  playTime: 0,
  currentLevel: 'map',
  settings: { sfxVolume: 0.7, musicVolume: 0.5, vibration: true },
  createdAt: Date.now(),
  updatedAt: Date.now(),
});

export class SaveSystem {
  constructor() {
    this.data = null;
  }

  load() {
    try {
      const raw = localStorage.getItem(SAVE_KEY);
      this.data = raw ? { ...defaultSave(), ...JSON.parse(raw) } : defaultSave();
    } catch {
      this.data = defaultSave();
    }
    return this.data;
  }

  save() {
    this.data.updatedAt = Date.now();
    try {
      localStorage.setItem(SAVE_KEY, JSON.stringify(this.data));
    } catch (e) {
      console.warn('Save failed:', e);
    }
  }

  reset() {
    this.data = defaultSave();
    localStorage.removeItem(SAVE_KEY);
  }

  completeTopicId(topicId, score) {
    if (!this.data.completedTopics.includes(topicId)) {
      this.data.completedTopics.push(topicId);
    }
    this.data.quizScores[topicId] = Math.max(
      this.data.quizScores[topicId] ?? 0,
      score
    );
    this.data.totalScore = Object.values(this.data.quizScores).reduce((a, b) => a + b, 0);
    this.save();
  }

  awardBadge(badgeId) {
    if (!this.data.badges.includes(badgeId)) {
      this.data.badges.push(badgeId);
      this.save();
      return true;
    }
    return false;
  }

  isTopicComplete(topicId) {
    return this.data.completedTopics.includes(topicId);
  }

  get(key) { return this.data?.[key]; }
  set(key, value) { this.data[key] = value; this.save(); }

  addPlayTime(seconds) {
    this.data.playTime += seconds;
  }
}

export const saveSystem = new SaveSystem();
