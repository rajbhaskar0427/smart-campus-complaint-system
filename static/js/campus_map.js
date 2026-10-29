// Campus Digital Twin & Interactive Map Controller

const CAMPUS_BUILDING_METADATA = {
  'Block A - Academic': {
    name: 'Academic Block A',
    code: 'BLKA',
    desc: 'Main engineering lecture theatres, faculty cabins, dean offices, and seminar halls.',
    floors: 'Ground + 4 Floors',
    defaultCategory: 'Electricity & Lighting',
    commonRooms: ['Room 101 - Smart Classroom', 'Room 204 - Lecture Hall', 'Room 302 - Tutorial Room', 'Dean Office Corridor']
  },
  'Block B - CS Labs': {
    name: 'Block B - CSE & IT Complex',
    code: 'BLKB',
    desc: 'Advanced computing labs, AI/ML center, high-speed campus server room, and network NOC.',
    floors: 'Ground + 3 Floors',
    defaultCategory: 'Internet & WiFi',
    commonRooms: ['CS Lab 1 - Systems Lab', 'CS Lab 2 - Software Dev', 'Room 304 - High Performance Lab', 'Server Room 301']
  },
  'Central Library': {
    name: 'Dr. A.P.J. Abdul Kalam Central Library',
    code: 'LIB',
    desc: 'Multi-tier digital repository, air-conditioned reading halls, journal archive, and reference center.',
    floors: 'Ground + 2 Floors',
    defaultCategory: 'Library Facilities',
    commonRooms: ['1st Floor Digital Reading Section', 'Ground Floor Stack Room', '2nd Floor Quiet Study Hall']
  },
  'Boys Hostel 1': {
    name: 'Ramanujan Boys Hostel (Block 1)',
    code: 'HSTL1',
    desc: 'Student residential quarters, common recreation rooms, gym, and dining hall.',
    floors: 'Ground + 4 Floors',
    defaultCategory: 'Water Supply',
    commonRooms: ['2nd Floor Common Washroom', 'Ground Floor Mess', 'Room 214 - Student Wing', 'Water Cooler Bay']
  },
  'Girls Hostel': {
    name: 'Kalpana Chawla Girls Hostel',
    code: 'GHSTL',
    desc: 'Secure residential facility for female scholars, study lounge, and indoor games room.',
    floors: 'Ground + 4 Floors',
    defaultCategory: 'Security & Safety',
    commonRooms: ['Wing B Fire Exit Staircase', 'Floor 1 Study Room', 'Corridor Lighting Node']
  },
  'Student Cafeteria': {
    name: 'Campus Food Court & Cafeteria',
    code: 'CAFE',
    desc: 'Multi-cuisine student canteen, coffee kiosk, and faculty dining area.',
    floors: 'Ground Floor Pavilion',
    defaultCategory: 'Cleanliness & Sanitation',
    commonRooms: ['Ground Floor Food Court', 'Juice Stall Area', 'Main Dining Hall']
  },
  'Sports Arena': {
    name: 'Lloyd Sports & Recreation Pavilion',
    code: 'SPORTS',
    desc: 'Basketball courts, indoor badminton arena, athletic turf, and gymnasium.',
    floors: 'Ground Level Arena',
    defaultCategory: 'Civil & Infrastructure',
    commonRooms: ['Indoor Badminton Court', 'Main Turf Lighting Pole', 'Locker Room']
  },
  'Campus Substation': {
    name: '11kV Electrical Substation & Genset Yard',
    code: 'SUBST',
    desc: 'High-voltage transformers, automatic DG synchronizers, and solar inverter array.',
    floors: 'Restricted Facility',
    defaultCategory: 'Electricity & Lighting',
    commonRooms: ['Yard Primary Incomer', 'Transformer Bay 2', 'UPS Battery Room']
  }
};

function selectBuilding(buildingKey) {
  const meta = CAMPUS_BUILDING_METADATA[buildingKey] || {
    name: buildingKey,
    code: 'GEN',
    desc: 'Campus infrastructure facility.',
    floors: 'Multi-level',
    defaultCategory: 'Other Facilities'
  };

  // Update Drawer UI
  const titleEl = document.getElementById('drawer-building-title');
  const descEl = document.getElementById('drawer-building-desc');
  const btnReport = document.getElementById('drawer-btn-report');
  const btnFilter = document.getElementById('drawer-btn-filter');

  if (titleEl) titleEl.innerText = meta.name;
  if (descEl) descEl.innerText = `${meta.desc} (${meta.floors})`;

  if (btnReport) {
    btnReport.href = `/submit?building=${encodeURIComponent(buildingKey)}&category=${encodeURIComponent(meta.defaultCategory || '')}`;
  }

  // Highlight SVG element
  document.querySelectorAll('.building-polygon').forEach(poly => {
    if (poly.getAttribute('data-building') === buildingKey) {
      poly.style.fill = '#2563eb';
      poly.style.stroke = '#38bdf8';
      poly.style.strokeWidth = '3px';
    } else {
      poly.style.fill = '#1e293b';
      poly.style.stroke = '#475569';
      poly.style.strokeWidth = '1.5px';
    }
  });

  // Filter complaints list in simulation view
  const complaintItems = document.querySelectorAll('.building-complaint-row');
  let matched = 0;
  complaintItems.forEach(item => {
    if (item.getAttribute('data-building') === buildingKey) {
      item.style.display = '';
      matched++;
    } else {
      item.style.display = 'none';
    }
  });

  const countBadge = document.getElementById('drawer-building-count');
  if (countBadge) {
    countBadge.innerText = `${matched} Active Tickets`;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  // Bind hover/click on all interactive SVG buildings
  document.querySelectorAll('.building-polygon').forEach(poly => {
    poly.addEventListener('click', () => {
      const bKey = poly.getAttribute('data-building');
      selectBuilding(bKey);
    });
  });

  // Default select Block B
  if (document.querySelector('.building-polygon')) {
    selectBuilding('Block B - CS Labs');
  }
});
