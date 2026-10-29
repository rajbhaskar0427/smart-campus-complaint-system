// Smart Campus Complaint System - Main Client JavaScript

document.addEventListener('DOMContentLoaded', function () {
  initDuplicateDetector();
  initStarRating();
  initTableSearch();
  initModalTriggers();
});

// Toast notification helper
function showToast(message, type = 'info') {
  let container = document.getElementById('toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'toast-container';
    container.style.cssText = `
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 99999;
      display: flex;
      flex-direction: column;
      gap: 10px;
    `;
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  const bgMap = {
    success: '#10b981',
    danger: '#ef4444',
    warning: '#f59e0b',
    info: '#2563eb'
  };

  toast.style.cssText = `
    background: ${bgMap[type] || '#1e293b'};
    color: #ffffff;
    padding: 12px 20px;
    border-radius: 10px;
    font-size: 0.9rem;
    font-weight: 600;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    display: flex;
    align-items: center;
    gap: 10px;
    animation: toastSlideIn 0.3s ease;
    max-width: 380px;
  `;
  toast.innerHTML = `<span>🔔</span> <span>${message}</span>`;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}

// 1. Real-time Duplicate Complaint Detector
function initDuplicateDetector() {
  const titleInput = document.getElementById('title');
  const buildingSelect = document.getElementById('building_block');
  const categorySelect = document.getElementById('category');
  const alertBox = document.getElementById('duplicate-alert-box');
  const duplicatesList = document.getElementById('duplicates-list');

  if (!titleInput || !buildingSelect || !categorySelect || !alertBox) return;

  let debounceTimer;

  function runCheck() {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
      const title = titleInput.value.trim();
      const building = buildingSelect.value;
      const category = categorySelect.value;

      if (!building || !category || title.length < 4) {
        alertBox.classList.remove('show');
        return;
      }

      fetch('/api/check-duplicates', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          title: title,
          building_block: building,
          category: category
        })
      })
      .then(res => res.json())
      .then(data => {
        if (data.duplicates && data.duplicates.length > 0) {
          alertBox.classList.add('show');
          duplicatesList.innerHTML = data.duplicates.map(d => `
            <div style="background: white; border: 1px solid #fde68a; border-radius: 8px; padding: 10px 14px; margin-top: 8px; display: flex; justify-content: space-between; align-items: center;">
              <div>
                <a href="/track/${d.ticket_id}" target="_blank" style="font-weight: 700; color: #1e40af; text-decoration: none;">#${d.ticket_id}</a>: 
                <span style="font-weight: 600; color: #1e293b;">${d.title}</span>
                <div style="font-size: 0.78rem; color: #64748b; margin-top: 2px;">
                  📍 ${d.room} | Status: <b>${d.status}</b> | Match: <span style="color: #b45309; font-weight: bold;">${d.confidence}%</span>
                </div>
              </div>
              <button type="button" class="btn btn-sm btn-outline" onclick="upvoteTicket('${d.ticket_id}', this)">
                👍 Upvote (${d.upvotes})
              </button>
            </div>
          `).join('');
        } else {
          alertBox.classList.remove('show');
        }
      })
      .catch(err => console.error('Duplicate check error:', err));
    }, 400);
  }

  titleInput.addEventListener('input', runCheck);
  buildingSelect.addEventListener('change', runCheck);
  categorySelect.addEventListener('change', runCheck);
}

// Upvote existing complaint
function upvoteTicket(ticketId, btn) {
  fetch(`/api/upvote/${ticketId}`, { method: 'POST' })
    .then(r => r.json())
    .then(data => {
      if (data.success) {
        btn.innerHTML = `👍 Upvoted (${data.upvotes})`;
        btn.classList.remove('btn-outline');
        btn.classList.add('btn-success');
        showToast(`You upvoted ticket #${ticketId}. The priority weight has increased!`, 'success');
      }
    });
}

// 2. Interactive Star Rating Picker
function initStarRating() {
  const starContainer = document.getElementById('star-picker');
  const ratingInput = document.getElementById('rating-input');
  if (!starContainer || !ratingInput) return;

  const stars = starContainer.querySelectorAll('.star');

  stars.forEach(star => {
    star.addEventListener('mouseenter', () => {
      const val = parseInt(star.getAttribute('data-value'));
      highlightStars(val);
    });

    star.addEventListener('click', () => {
      const val = parseInt(star.getAttribute('data-value'));
      ratingInput.value = val;
      highlightStars(val);
      const textHint = document.getElementById('rating-text');
      if (textHint) {
        const labels = ['', 'Poor', 'Fair', 'Satisfactory', 'Very Good', 'Outstanding'];
        textHint.innerText = `${val} Stars - ${labels[val]}`;
      }
    });
  });

  starContainer.addEventListener('mouseleave', () => {
    const current = parseInt(ratingInput.value) || 5;
    highlightStars(current);
  });

  function highlightStars(count) {
    stars.forEach(s => {
      const v = parseInt(s.getAttribute('data-value'));
      if (v <= count) {
        s.classList.add('filled');
      } else {
        s.classList.remove('filled');
      }
    });
  }

  // Initial highlight
  highlightStars(parseInt(ratingInput.value) || 5);
}

// 3. Client Table Search & Filter
function initTableSearch() {
  const searchInput = document.getElementById('client-table-search');
  if (!searchInput) return;

  const table = document.querySelector('.data-table tbody');
  if (!table) return;

  searchInput.addEventListener('input', function () {
    const query = this.value.toLowerCase().trim();
    const rows = table.querySelectorAll('tr');

    rows.forEach(row => {
      const text = row.innerText.toLowerCase();
      if (text.includes(query)) {
        row.style.display = '';
      } else {
        row.style.display = 'none';
      }
    });
  });
}

// 4. Modal Management
function initModalTriggers() {
  document.querySelectorAll('[data-modal]').forEach(trigger => {
    trigger.addEventListener('click', () => {
      const modalId = trigger.getAttribute('data-modal');
      openModal(modalId);
    });
  });

  document.querySelectorAll('.modal-close').forEach(btn => {
    btn.addEventListener('click', () => {
      const overlay = btn.closest('.modal-overlay');
      if (overlay) overlay.classList.remove('active');
    });
  });
}

function openModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.add('active');
}

function closeModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.remove('active');
}
