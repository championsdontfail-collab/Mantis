# Forest Treasure Quest — immutable UI module rules

Approved by the project owner on 2026-10-21. Preserve the exact approved forest, squirrel, bird, wooden signs, and answer-button artwork. No redraws, image crops that cut off the squirrel, overlays covering existing text, or replacement graphics.

## Answer button module
Every answer is ONE component consisting of the original wooden button asset, its centered label, and its click handler. Do not position the label independently of the button or use absolute page-level coordinates for the label. The four buttons must be instances of the same component, using a shared CSS class and layout container. Use a single source of truth for spacing, sizing, and font.

```html
<div class="answers" id="answers">
  <!-- render four instances of the same button component -->
  <button class="answer" type="button" data-choice="0"><span class="answer__label">gave</span></button>
</div>
```

```css
.answers { display:grid; grid-template-columns:1fr; gap:12px; width:100%; }
.answer {
  position:relative; display:grid; place-items:center;
  width:100%; min-height:64px; padding:10px 18px;
  background-image:var(--original-wood-button);
  background-size:100% 100%; background-repeat:no-repeat;
  border:0; cursor:pointer;
}
.answer__label {
  position:static; display:block; max-width:100%;
  text-align:center; line-height:1.15; overflow-wrap:anywhere;
  font:700 clamp(19px,5vw,27px) Georgia,serif; color:#4c2b16;
}
```

The parent layout can scale with viewport width; artwork and label always scale/align together. No independent top/left for each answer label. Answer variants must be similar forms of the SAME irregular verb; exactly one correct answer. Do not show a green state before selection.

## Other components
- Forest background: single original image, rendered with preserved aspect ratio and no replacement/blurred collage.
- Squirrel: independent original art, fully visible with object-fit:contain; poses vary without cropping.
- Question parchment: original blank artwork with one dynamic question label within its designated blank area.
- Feedback: one original blank panel for dynamic correct forms, one separate squirrel speech element, one working Next button; never layer on printed words.
- Results: one actual action button and no duplicate text-baked controls.

## Quality gates
Test on narrow Android viewport: all four labels centered on their respective wooden buttons, no text over the squirrel, no overlays, no clipped artwork, 20 questions, correct/wrong transitions, Next, score, restart. Never claim visual testing was completed without screenshots or browser evidence.

Status: specification saved. It must be applied to the next build; this document does not itself modify the currently deployed game.
