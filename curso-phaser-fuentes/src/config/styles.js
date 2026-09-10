// Fuente web cargada en index.html; los fallbacks garantizan legibilidad
export const FONT = '"Nunito", "Segoe UI", system-ui, sans-serif';

// Sombra dura (blur:0) → mejora contraste SIN el halo borroso del stroke
const SH = { offsetX: 1, offsetY: 1, color: '#000000', blur: 0, fill: true };

// Estilos predefinidos — úsalos como spread: this.add.text(x,y,'txt', T.body())
export const T = {
  title:   (sz = 26) => ({ fontFamily: FONT, fontSize: `${sz}px`, fill: '#f5c842', fontStyle: 'bold', shadow: SH }),
  header:  (sz = 18) => ({ fontFamily: FONT, fontSize: `${sz}px`, fill: '#ffffff', fontStyle: 'bold', shadow: SH }),
  body:    (sz = 15) => ({ fontFamily: FONT, fontSize: `${sz}px`, fill: '#ffffff', shadow: SH }),
  muted:   (sz = 13) => ({ fontFamily: FONT, fontSize: `${sz}px`, fill: '#e8f4ff', shadow: SH }),
  hint:    (sz = 12) => ({ fontFamily: FONT, fontSize: `${sz}px`, fill: '#cce4f8', shadow: SH }),
  success: (sz = 16) => ({ fontFamily: FONT, fontSize: `${sz}px`, fill: '#55ee99', fontStyle: 'bold', shadow: SH }),
  danger:  (sz = 16) => ({ fontFamily: FONT, fontSize: `${sz}px`, fill: '#ff7777', fontStyle: 'bold', shadow: SH }),
  gold:    (sz = 16) => ({ fontFamily: FONT, fontSize: `${sz}px`, fill: '#f5c842', fontStyle: 'bold', shadow: SH }),
  score:   (sz = 16) => ({ fontFamily: FONT, fontSize: `${sz}px`, fill: '#55ee99', fontStyle: 'bold', shadow: SH }),
};
