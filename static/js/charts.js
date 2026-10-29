// Self-Contained SVG/Canvas Chart Engine (Zero CDN Dependency - 100% Offline)

// 1. Donut Chart Generator
function renderDonutChart(containerId, data, colors) {
  const container = document.getElementById(containerId);
  if (!container || !data || data.length === 0) return;

  const total = data.reduce((acc, cur) => acc + cur.value, 0);
  if (total === 0) {
    container.innerHTML = '<div style="text-align:center; padding: 40px; color:#94a3b8;">No data available</div>';
    return;
  }

  const size = 240;
  const strokeWidth = 36;
  const radius = (size - strokeWidth) / 2;
  const center = size / 2;
  const circumference = 2 * Math.PI * radius;

  let offset = 0;
  let paths = '';

  data.forEach((item, index) => {
    const color = colors[index % colors.length];
    const ratio = item.value / total;
    const dashLength = ratio * circumference;
    const dashSpace = circumference - dashLength;

    paths += `
      <circle
        cx="${center}" cy="${center}" r="${radius}"
        fill="transparent"
        stroke="${color}"
        stroke-width="${strokeWidth}"
        stroke-dasharray="${dashLength} ${dashSpace}"
        stroke-dashoffset="-${offset}"
        style="transition: stroke-dashoffset 0.8s ease;"
      >
        <title>${item.label}: ${item.value} (${Math.round(ratio * 100)}%)</title>
      </circle>
    `;
    offset += dashLength;
  });

  // Legend
  let legend = '<div style="display:flex; flex-direction:column; gap:6px; justify-content:center; margin-left: 20px;">';
  data.forEach((item, index) => {
    const color = colors[index % colors.length];
    const pct = Math.round((item.value / total) * 100);
    legend += `
      <div style="display:flex; align-items:center; gap:8px; font-size:0.85rem;">
        <span style="width:12px; height:12px; border-radius:3px; background:${color}; display:inline-block;"></span>
        <span style="font-weight:600; color:#1e293b;">${item.label}</span>
        <span style="color:#64748b; margin-left:auto;">${item.value} (${pct}%)</span>
      </div>
    `;
  });
  legend += '</div>';

  container.innerHTML = `
    <div style="display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:16px;">
      <svg width="${size}" height="${size}" viewBox="0 0 ${size} ${size}" style="transform: rotate(-90deg);">
        ${paths}
        <text x="${center}" y="${center}" text-anchor="middle" dominant-baseline="middle"
              style="transform: rotate(90deg); transform-origin: center; font-size: 24px; font-weight: 800; fill: #0f172a;">
          ${total}
        </text>
        <text x="${center}" y="${center + 20}" text-anchor="middle" dominant-baseline="middle"
              style="transform: rotate(90deg); transform-origin: center; font-size: 11px; font-weight: 600; fill: #64748b; text-transform: uppercase;">
          Total
        </text>
      </svg>
      ${legend}
    </div>
  `;
}

// 2. Horizontal Bar Chart Generator
function renderHorizontalBarChart(containerId, data, defaultColor = '#3b82f6') {
  const container = document.getElementById(containerId);
  if (!container || !data || data.length === 0) return;

  const maxValue = Math.max(...data.map(d => d.value), 1);

  let html = '<div style="display:flex; flex-direction:column; gap:12px; width:100%;">';
  data.forEach(item => {
    const pct = Math.round((item.value / maxValue) * 100);
    html += `
      <div>
        <div style="display:flex; justify-content:space-between; margin-bottom:4px; font-size:0.85rem; font-weight:600;">
          <span style="color:#1e293b;">${item.label}</span>
          <span style="color:#3b82f6; font-weight:700;">${item.value} issues</span>
        </div>
        <div style="width:100%; background:#e2e8f0; height:12px; border-radius:6px; overflow:hidden;">
          <div style="width:${pct}%; background:${item.color || defaultColor}; height:100%; border-radius:6px; transition: width 0.8s ease;"></div>
        </div>
      </div>
    `;
  });
  html += '</div>';

  container.innerHTML = html;
}
