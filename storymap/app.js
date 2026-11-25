(async function () {
  'use strict';

  const byId = (id) => document.getElementById(id);
  const els = {
    chapter: byId('chapter'), title: byId('story-title'), period: byId('period'),
    place: byId('place'), virus: byId('virus'), summary: byId('summary'),
    caseCount: byId('case-count'), deathCount: byId('death-count'),
    tollContext: byId('toll-context'), tollNote: byId('toll-note'), tollSource: byId('toll-source'),
    storyScroll: document.querySelector('.story-scroll'),
    photoImage: byId('photo-image'), photoCaption: byId('photo-caption'),
    photoCreator: byId('photo-creator'), photoSource: byId('photo-source'),
    photoLicense: byId('photo-license'), videoLink: byId('video-link'),
    videoNote: byId('video-note'), videoCredit: byId('video-credit'),
    question: byId('question'), sourceLink: byId('source-link'), sourceLabel: byId('source-label'),
    visualLink: byId('visual-link'), visualLabel: byId('visual-label'),
    contextLink: byId('context-link'), contextLabel: byId('context-label'),
    analysisLink: byId('analysis-link'), analysisLabel: byId('analysis-label'),
    stopNumber: byId('stop-number'), progress: byId('progress-text'),
    prev: byId('prev-button'), next: byId('next-button'),
    slider: byId('year-slider'), timelineCurrent: byId('timeline-current'),
    timelinePeriod: byId('timeline-period'), timelineEvents: byId('timeline-events'),
    stopList: byId('stop-list'), mapTitle: byId('map-caption-title'),
    mapSubtitle: byId('map-caption-subtitle'), africa: byId('africa-button'),
    mapError: byId('map-error')
  };

  let stops;
  try {
    const response = await fetch('./stops.json');
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    stops = await response.json();
    if (!Array.isArray(stops) || !stops.length) throw new Error('No tour stops found');
  } catch (error) {
    els.summary.textContent = 'The tour data could not load. Please use the linked StoryMap plan and references in the repository.';
    els.mapError.hidden = false;
    els.prev.disabled = true;
    els.next.disabled = true;
    console.error('StoryMap data loading failed:', error);
    return;
  }

  const mapAvailable = typeof window.L !== 'undefined';
  let map = null;
  const markers = [];
  if (mapAvailable) {
    map = L.map('map', { zoomControl: false, scrollWheelZoom: false, minZoom: 3, maxZoom: 13 }).setView([0, 20], 3);
    L.control.zoom({ position: 'bottomright' }).addTo(map);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener noreferrer">OpenStreetMap contributors</a> · ODbL'
    }).addTo(map);
  } else {
    els.mapError.hidden = false;
  }

  function iconFor(stop, active) {
    const species = stop.virus === 'Sudan virus' ? 'sudan' : stop.virus === 'Bundibugyo virus' ? 'bundibugyo' : 'ebola';
    return L.divIcon({ className: '', html: `<span class="tour-marker ${species}${active ? ' active' : ''}" aria-hidden="true"></span>`, iconSize: [22, 22], iconAnchor: [11, 11] });
  }

  if (map) {
    stops.forEach((stop, index) => {
      const marker = L.marker([stop.lat, stop.lon], { icon: iconFor(stop, false), keyboard: true, title: `${stop.year}: ${stop.place}` }).addTo(map);
      marker.bindTooltip(`${stop.year} · ${stop.place}`);
      marker.on('click', () => selectStop(index));
      markers.push(marker);
    });
  }

  const timelineButtons = [];
  const listButtons = [];
  stops.forEach((stop, index) => {
    const chip = document.createElement('button');
    chip.type = 'button';
    chip.textContent = `${stop.year} · ${stop.place}`;
    chip.setAttribute('aria-label', `Open ${stop.year} stop: ${stop.title}, ${stop.place}`);
    chip.addEventListener('click', () => selectStop(index));
    els.timelineEvents.appendChild(chip);
    timelineButtons.push(chip);

    const item = document.createElement('li');
    const button = document.createElement('button');
    button.type = 'button';
    button.textContent = `${stop.year} — ${stop.title}`;
    button.addEventListener('click', () => selectStop(index));
    item.appendChild(button);
    els.stopList.appendChild(item);
    listButtons.push(button);
  });

  let selectedIndex = -1;
  function selectStop(index, options = {}) {
    if (!Number.isInteger(index) || index < 0 || index >= stops.length) return;
    const stop = stops[index];
    selectedIndex = index;
    els.chapter.textContent = stop.chapter;
    els.title.textContent = stop.title;
    els.period.textContent = stop.period;
    els.place.textContent = `${stop.place} · ${stop.country}`;
    els.virus.textContent = stop.virus;
    els.caseCount.textContent = stop.metrics.cases.toLocaleString('en-US');
    els.deathCount.textContent = stop.metrics.deaths.toLocaleString('en-US');
    els.tollContext.textContent = `${stop.metrics.status} · ${stop.metrics.scope} · ${stop.metrics.definition}`;
    els.tollNote.textContent = stop.metrics.note || '';
    els.tollNote.hidden = !stop.metrics.note;
    els.tollSource.href = stop.metrics.sourceUrl;
    els.tollSource.textContent = `${stop.metrics.sourceLabel} ↗`;
    els.summary.textContent = stop.summary;
    els.photoImage.alt = stop.photo.alt;
    els.photoImage.src = stop.photo.src;
    els.photoCaption.textContent = stop.photo.caption;
    els.photoCreator.textContent = stop.photo.creator;
    els.photoSource.href = stop.photo.sourceUrl;
    els.photoSource.textContent = `${stop.photo.title} (${stop.photo.date})`;
    els.photoLicense.href = stop.photo.licenseUrl;
    els.photoLicense.textContent = stop.photo.license;
    els.videoLink.href = stop.video.url;
    els.videoLink.textContent = `${stop.video.title} ↗`;
    els.videoNote.textContent = stop.video.note;
    els.videoCredit.textContent = `${stop.video.publisher} · ${stop.video.date} · linked video`;
    els.storyScroll.scrollTop = 0;
    els.question.textContent = stop.question;
    els.sourceLink.href = stop.sourceUrl;
    els.sourceLabel.textContent = stop.source;
    els.visualLink.href = stop.visualUrl;
    els.visualLabel.textContent = stop.visual;
    els.contextLink.hidden = !stop.contextUrl;
    if (stop.contextUrl) {
      els.contextLink.href = stop.contextUrl;
      els.contextLabel.textContent = stop.context;
    }
    els.analysisLink.hidden = !stop.analysisUrl;
    if (stop.analysisUrl) {
      els.analysisLink.href = stop.analysisUrl;
      els.analysisLabel.textContent = stop.analysis;
    }
    els.stopNumber.textContent = `${String(index + 1).padStart(2, '0')} / ${String(stops.length).padStart(2, '0')}`;
    els.progress.textContent = `Stop ${index + 1} of ${stops.length}`;
    els.prev.disabled = index === 0;
    els.next.disabled = index === stops.length - 1;
    els.slider.value = String(stop.year);
    els.timelineCurrent.textContent = String(stop.year);
    els.timelinePeriod.textContent = stop.period;
    els.mapTitle.textContent = stop.place;
    els.mapSubtitle.textContent = `${stop.country} · approximate locator, not case coordinates`;

    timelineButtons.forEach((button, i) => {
      button.classList.toggle('active', i === index);
      if (i === index) button.setAttribute('aria-current', 'step');
      else button.removeAttribute('aria-current');
    });
    listButtons.forEach((button, i) => {
      if (i === index) button.setAttribute('aria-current', 'step');
      else button.removeAttribute('aria-current');
    });
    if (!options.fromSlider) timelineButtons[index].scrollIntoView({ block: 'nearest', inline: 'nearest', behavior: 'smooth' });

    if (map) {
      markers.forEach((marker, i) => { marker.setIcon(iconFor(stops[i], i === index)); marker.setZIndexOffset(i === index ? 1000 : 0); });
      const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      if (reducedMotion || options.initial) map.setView([stop.lat, stop.lon], stop.zoom, { animate: false });
      else map.flyTo([stop.lat, stop.lon], stop.zoom, { duration: 0.75 });
      requestAnimationFrame(() => map.invalidateSize());
    }
    if (!options.fromHash) history.replaceState(null, '', `#${encodeURIComponent(stop.id)}`);
  }

  els.prev.addEventListener('click', () => selectStop(selectedIndex - 1));
  els.next.addEventListener('click', () => selectStop(selectedIndex + 1));
  els.africa.addEventListener('click', () => { if (map) map.fitBounds([[-35, -18], [20, 51]], { padding: [25, 25] }); });
  els.slider.addEventListener('input', () => {
    const year = Number(els.slider.value);
    let nearest = 0;
    let distance = Infinity;
    stops.forEach((stop, index) => {
      const nextDistance = Math.abs(stop.year - year);
      if (nextDistance < distance) { nearest = index; distance = nextDistance; }
    });
    selectStop(nearest, { fromSlider: true });
  });
  window.addEventListener('hashchange', () => {
    const id = decodeURIComponent(location.hash.slice(1));
    const index = stops.findIndex((stop) => stop.id === id);
    if (index >= 0) selectStop(index, { fromHash: true });
  });
  document.addEventListener('keydown', (event) => {
    if (event.altKey || event.ctrlKey || event.metaKey || ['INPUT', 'TEXTAREA', 'BUTTON'].includes(document.activeElement?.tagName)) return;
    if (event.key === 'ArrowRight' && selectedIndex < stops.length - 1) selectStop(selectedIndex + 1);
    if (event.key === 'ArrowLeft' && selectedIndex > 0) selectStop(selectedIndex - 1);
  });

  const initialId = decodeURIComponent(location.hash.slice(1));
  const initialIndex = Math.max(0, stops.findIndex((stop) => stop.id === initialId));
  selectStop(initialIndex, { initial: true });
})();
