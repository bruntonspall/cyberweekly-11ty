export const url = process.env.URL || 'http://localhost:8080';
export const siteName = 'Cyberweekly';
export const siteDescription = 'A weekly roundup of interesting content from across the web that is of interest to people working in cyber security. Generally long form articles and blog posts, as well as links to outages, incidents and security bugs that you might find interesting. Presented with a small amount of editorial comment';
export const siteType = 'Blog'; // schema
export const locale = 'en_EN';
export const lang = 'en';
export const skipContent = 'Skip to content';
export const author = {
  name: 'Michael Brunton-Spall', // i.e. Lene Saile - page / blog author's name. Must be set.
  avatar: 'https://lh3.googleusercontent.com/a-/AOh14GgqmmzowdIw7ZjuJxhp5qimng30pwRTPCfUvUMQyk0=s96-c', // path to the author's avatar. In this case just using a favicon.
  email: 'michael@brunton-spall.co.uk', // i.e. hola@lenesaile.com - email of the author
  website: 'https://www.brunton-spall.co.uk', // i.e. https.://www.lenesaile.com - the personal site of the author
  fediverse: 'https://octodon.social/@bruntonspall' // used for highlighting journalism on the fediverse. Can be Mastodon, Flipboard, Threads, WordPress (with the ActivityPub plugin installed), PeerTube, Pixelfed, etc. https://blog.joinmastodon.org/2024/07/highlighting-journalism-on-mastodon/
};
export const creator = {
  name: 'Michael Brunton-Spall', // i.e. Lene Saile - creator's (developer) name.
  email: 'michael@brunton-spall.co.uk', // i.e. hola@lenesaile.com - email of the author
  website: 'https://www.brunton-spall.co.uk', // i.e. https.://www.lenesaile.com - the personal site of the author
  fediverse: 'https://octodon.social/@bruntonspall' // used for highlighting journalism on the fediverse. Can be Mastodon, Flipboard, Threads, WordPress (with the ActivityPub plugin installed), PeerTube, Pixelfed, etc. https://blog.joinmastodon.org/2024/07/highlighting-journalism-on-mastodon/
};
export const pathToSvgLogo = 'src/assets/svg/misc/logo.svg'; // used for favicon generation
export const themeColor = '#dd4462'; // used in manifest, for example primary color value
export const themeLight = '#f8f8f8'; // used for meta tag theme-color, if light colors are prefered. best use value set for light bg
export const themeDark = '#FBFBFB'; // used for meta tag theme-color, if dark colors are prefered. best use value set for dark bg
export const opengraph_default = '/assets/images/template/opengraph-default.jpg'; // fallback/default meta image
export const opengraph_default_alt =
  "Cyberweekly: A weekly roundup of interesting content from across the web that is of interest to people working in cyber security. Generally long form articles and blog posts, as well as links to outages, incidents and security bugs that you might find interesting. Presented with a small amount of editorial comment"; // alt text for default meta image"
export const blog = {
  // RSS feed
  name: 'Cyberweekly',
  description: 'A weekly roundup of interesting content from across the web that is of interest to people working in cyber security. Generally long form articles and blog posts, as well as links to outages, incidents and security bugs that you might find interesting. Presented with a small amount of editorial comment',
  // feed links are looped over in the head. You may add more to the array.
  feedLinks: [
    {
      title: 'Atom Feed',
      url: '/feed.xml',
      type: 'application/atom+xml'
    },
    {
      title: 'JSON Feed',
      url: '/feed.json',
      type: 'application/json'
    }
  ],
  // Tags
  tagSingle: 'Tag',
  tagPlural: 'Tags',
  tagMore: 'More tags:',
  // pagination
  paginationLabel: 'Blog',
  paginationPage: 'Page',
  paginationPrevious: 'Previous',
  paginationNext: 'Next',
  paginationNumbers: true
};
export const details = {
  aria: 'section controls',
  expand: 'expand all',
  collapse: 'collapse all'
};
export const navigation = {
  navLabel: 'Menu',
  ariaTop: 'Main',
  ariaBottom: 'Complementary',
  ariaPlatforms: 'Platforms',
  drawerNav: false
};
export const themeSwitch = {
  title: 'Theme',
  light: 'light',
  dark: 'dark'
};
export const viewRepo = {
  // this is for the view/edit on github link. The value in the package.json will be pulled in.
  allow: true,
  infoText: 'View this page on GitHub'
};
