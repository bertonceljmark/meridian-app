// Shared stage constants: bake.html renders the photo stage with these, index.html draws the live hero with
// the same camera and key light so the two line up pixel for pixel.
export const STAGE = {
  fov: 36, cam: [0, 1.33, 7.6], target: [0, 0.27, 0],
  bake: { w: 1290, h: 2796 },
  baseY: 0.0,                      // ledge top under the plinth, in bake space
  fit: { h: 1.75, w: 1.9 },        // every hero is scaled into this box
  fog: 0x0a0f18, fogDensity: 0.045,
  key: { i: 320, angle: 0.3, pos: [-2.6, 7.6, 4.6], target: [0, 0.6, 0] },
  pieces: [
    { path: 'assets/src/rock_09/rock_09.gltf', s: 32, r: [0, Math.PI / 2, 0], p: [0, -1.0, 0.2], k: 0.7 },
    { path: 'assets/src/mountainside/mountainside.gltf', s: 0.65, r: [0, Math.PI / 2 + 0.25, 0], p: [-1.25, -1.8, -3.8], k: 0.5 },
    { path: 'assets/src/mountainside/mountainside.gltf', s: 0.7, r: [0, -Math.PI / 2 - 0.3, 0], p: [1.35, -2.2, -5.0], k: 0.45 },
  ],
};
