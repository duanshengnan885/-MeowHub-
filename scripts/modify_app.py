import sys

js_code = '''
// --- 星喵互动情绪球 (Easter Egg) ---
document.addEventListener('DOMContentLoaded', () => {
    const orb = document.getElementById('dock-status-orb');
    if (orb) {
        orb.addEventListener('click', function(e) {
            // Click animation
            this.style.transform = 'scale(0.7)';
            setTimeout(() => this.style.transform = 'scale(1)', 150);

            const meows = ["喵~", "喵呜!", "呼噜噜~", "🐾", "💖", "✨", "🐟", "干饭!"];
            const text = meows[Math.floor(Math.random() * meows.length)];
            
            const floatEl = document.createElement('div');
            floatEl.textContent = text;
            floatEl.style.position = 'fixed';
            floatEl.style.left = (e.clientX - 10) + 'px';
            floatEl.style.top = (e.clientY - 15) + 'px';
            floatEl.style.color = '#a855f7';
            floatEl.style.fontWeight = 'bold';
            floatEl.style.fontSize = '12px';
            floatEl.style.pointerEvents = 'none';
            floatEl.style.zIndex = '99999';
            floatEl.style.transition = 'all 1s ease-out';
            floatEl.style.textShadow = '0 2px 4px rgba(0,0,0,0.3)';
            
            document.body.appendChild(floatEl);
            
            // Force reflow
            floatEl.getBoundingClientRect();
            
            // Random float trajectory
            floatEl.style.transform = 	ranslate(px, -px) scale(1.3);
            floatEl.style.opacity = '0';
            
            setTimeout(() => {
                if (floatEl.parentNode) {
                    floatEl.parentNode.removeChild(floatEl);
                }
            }, 1000);
        });
    }
});
'''

with open('ai_ui_assistant/app.js', 'a', encoding='utf-8') as f:
    f.write("\n" + js_code)

print("Easter egg added to app.js")
