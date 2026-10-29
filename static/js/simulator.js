// Live Simulation & Incident Response Controller

function appendConsoleLog(tag, message) {
  const consoleEl = document.getElementById('sim-live-console');
  if (!consoleEl) return;

  const now = new Date();
  const timeStr = now.toLocaleTimeString();

  const entry = document.createElement('div');
  entry.className = 'console-entry';
  entry.innerHTML = `
    <span class="console-ts">[${timeStr}]</span>
    <span class="console-tag">[${tag}]</span>
    <span>${message}</span>
  `;

  consoleEl.appendChild(entry);
  consoleEl.scrollTop = consoleEl.scrollHeight;
}

// 1. Simulate IoT Sensor Trigger
function runIoTSimulation(sensorId = null) {
  appendConsoleLog('TELEMETRY_POLL', 'Querying wireless campus sensor nodes...');
  
  fetch('/api/simulation/trigger-iot', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ sensor_id: sensorId })
  })
  .then(r => r.json())
  .then(data => {
    if (data.success) {
      appendConsoleLog('IOT_ANOMALY', `Anomaly detected on node: ${data.sensor.name}. Auto-dispatch ticket created: ${data.ticket_id}`);
      showToast(`⚡ IoT Alert: ${data.sensor.name} breached safety threshold! Ticket #${data.ticket_id} created.`, 'danger');
      setTimeout(() => window.location.reload(), 2000);
    } else {
      appendConsoleLog('IOT_INFO', data.message || 'Telemetry nominal.');
    }
  })
  .catch(err => {
    appendConsoleLog('ERROR', 'Failed to connect to IoT gateway emulator.');
  });
}

// 2. Simulate SLA Auto-Escalation Engine
function runAutoEscalation() {
  appendConsoleLog('SLA_ENGINE', 'Scanning active tickets against SLA resolution matrix...');

  fetch('/api/simulation/auto-escalate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' }
  })
  .then(r => r.json())
  .then(data => {
    if (data.success) {
      appendConsoleLog('ESCALATION_TRIGGERED', `Ticket #${data.ticket_id} exceeded response window. Auto-escalated to: ${data.escalated_to}`);
      showToast(`🚨 Auto-Escalation: Ticket #${data.ticket_id} escalated to Dean / Chief Proctor!`, 'warning');
      setTimeout(() => window.location.reload(), 2000);
    } else {
      appendConsoleLog('SLA_OK', data.message);
      showToast(data.message, 'info');
    }
  })
  .catch(err => {
    appendConsoleLog('ERROR', 'SLA daemon offline.');
  });
}

// 3. Simulate Field Technician Dispatch & Resolve
function runWorkerResolveDemo() {
  appendConsoleLog('DISPATCH', 'Simulating field technician assignment and closure...');

  fetch('/api/simulation/resolve-demo', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' }
  })
  .then(r => r.json())
  .then(data => {
    if (data.success) {
      appendConsoleLog('STATUS_UPDATE', `Ticket #${data.ticket_id} marked RESOLVED. Remarks: "${data.remarks}"`);
      showToast(`✅ Field worker resolved Ticket #${data.ticket_id}! Verification pending.`, 'success');
      setTimeout(() => window.location.reload(), 2000);
    } else {
      appendConsoleLog('NOTICE', data.message);
      showToast(data.message, 'info');
    }
  })
  .catch(err => {
    appendConsoleLog('ERROR', 'Technician dispatch endpoint error.');
  });
}

document.addEventListener('DOMContentLoaded', () => {
  appendConsoleLog('SYSTEM_READY', 'Smart Campus Digital Twin & SLA Daemon initialized. Real-time telemetry active.');
});
