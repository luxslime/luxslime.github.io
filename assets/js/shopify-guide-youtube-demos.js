(function () {
  var MAP = {"/guides/block-po-box-billing-address/": {"id": "7zwHWfp_UgM", "url": "https://www.youtube.com/watch?v=7zwHWfp_UgM", "title": "AddressFence PO Box billing demo on YouTube"}, "/guides/prop-65-product-page-warning-2028/": {"id": "REdc4uJ8ZW0", "url": "https://www.youtube.com/watch?v=REdc4uJ8ZW0", "title": "Prop 65 Warning Manager demo on YouTube"}, "/guides/access-audit-shopify-admin/": {"id": "3xlq4BLK0mw", "url": "https://www.youtube.com/watch?v=3xlq4BLK0mw", "title": "Access Audit Guard demo on YouTube"}, "/guides/b2b-po-number-required/": {"id": "qdqarxVWoS8", "url": "https://youtu.be/qdqarxVWoS8", "title": "B2B Terms and PO Guard demo on YouTube"}, "/guides/agentic-catalog-readiness/": {"id": "NhIx9HC0q5s", "url": "https://youtu.be/NhIx9HC0q5s", "title": "Agentic Catalog Readiness demo on YouTube"}, "/guides/eu-generic-green-claims-ban/": {"id": "X7UZmBMEN1U", "url": "https://youtu.be/X7UZmBMEN1U", "title": "Green Claims Guard demo on YouTube"}, "/guides/eudr-dds-lot-registry/": {"id": "b3W12Nj6GTM", "url": "https://youtu.be/b3W12Nj6GTM", "title": "EUDR Records Manager demo on YouTube"}, "/guides/clp-hazard-product-page/": {"id": "Qt9fgPI_11A", "url": "https://youtu.be/Qt9fgPI_11A", "title": "CLPLens hazard display demo on YouTube"}, "/guides/textile-fibre-label-eu/": {"id": "0_23ZYHpbd8", "url": "https://youtu.be/0_23ZYHpbd8", "title": "FibreLedger textile labels demo on YouTube"}, "/guides/fic-food-allergen-label/": {"id": "ouICrksWHcA", "url": "https://youtu.be/ouICrksWHcA", "title": "EU Food Info Guard demo on YouTube"}, "/guides/cra-duty-records-eu/": {"id": "eyGzlHi3G50", "url": "https://youtu.be/eyGzlHi3G50", "title": "CRALedger duty records demo on YouTube"}, "/guides/repair-proof-eu-right-to-repair/": {"id": "-l0pRLEjVfs", "url": "https://youtu.be/-l0pRLEjVfs", "title": "RepairProof EU demo on YouTube"}};
  var path = location.pathname;
  if (path.slice(-1) !== "/") path += "/";
  var demo = MAP[path];
  if (!demo) return;
  if (document.querySelector(".demo-embed, h2.shopify-yt-demo")) return;
  var style = document.createElement("style");
  style.textContent = ".demo-embed{position:relative;width:100%;height:0;padding-bottom:56.25%;margin:0 0 16px;overflow:hidden;border:1px solid #d9dde5;background:#000}.demo-embed iframe{position:absolute;top:0;left:0;width:100%;height:100%;border:0}";
  document.head.appendChild(style);
  var h2 = document.createElement("h2");
  h2.className = "shopify-yt-demo";
  h2.textContent = "Demo";
  var p = document.createElement("p");
  p.textContent = "Short walkthrough of the app flow. Then follow the start path below.";
  var wrap = document.createElement("div");
  wrap.className = "demo-embed";
  var iframe = document.createElement("iframe");
  iframe.src = "https://www.youtube.com/embed/" + demo.id;
  iframe.title = demo.title;
  iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
  iframe.setAttribute("allowfullscreen", "");
  iframe.loading = "lazy";
  iframe.referrerPolicy = "strict-origin-when-cross-origin";
  wrap.appendChild(iframe);
  var linkP = document.createElement("p");
  var a = document.createElement("a");
  a.href = demo.url;
  a.textContent = "Open the demo on YouTube";
  linkP.appendChild(a);
  var main = document.querySelector("main");
  if (!main) return;
  var firstH2 = main.querySelector("h2");
  if (firstH2) {
    main.insertBefore(h2, firstH2);
    main.insertBefore(p, firstH2);
    main.insertBefore(wrap, firstH2);
    main.insertBefore(linkP, firstH2);
  } else {
    main.appendChild(h2);
    main.appendChild(p);
    main.appendChild(wrap);
    main.appendChild(linkP);
  }
})();
