// Shared stage constants: one fixed camera and key light for every hero and every stage.
export const STAGE = {
  fov: 36, cam: [0, 1.33, 7.6], target: [0, 0.27, 0],
  fit: { h: 1.75, w: 1.9 },        // every hero is scaled into this box
  key: { i: 320, angle: 0.3, pos: [-2.6, 7.6, 4.6], target: [0, 0.6, 0] },
};
