import { Issue } from "../interfaces";
import { ProjectReference } from "src/app/api/projects/projects-api.interfaces";

interface APIProjectReference extends Omit<ProjectReference, "id"> {
  id: string;
}

interface APIIssue extends Omit<Issue, "project"> {
  project: APIProjectReference;
}

export const apiIssueList: APIIssue[] = [
  {
    lastSeen: "2021-02-19T18:56:01.952Z",
    numComments: 0,
    userCount: 0,
    stats: {
      "24h": [
        [1613678400, 0],
        [1613682000, 0],
        [1613685600, 0],
        [1613689200, 0],
        [1613692800, 0],
        [1613696400, 0],
        [1613700000, 0],
        [1613703600, 0],
        [1613707200, 0],
        [1613710800, 0],
        [1613714400, 0],
        [1613718000, 0],
        [1613721600, 0],
        [1613725200, 0],
        [1613728800, 0],
        [1613732400, 0],
        [1613736000, 0],
        [1613739600, 0],
        [1613743200, 0],
        [1613746800, 0],
        [1613750400, 0],
        [1613754000, 0],
        [1613757600, 1],
        [1613761200, 0],
      ],
    },
    culprit: "/level-fatal/",
    title: "fatal custom level",
    id: 240,
    assignedTo: null,
    logger: null,
    type: "default",
    annotations: [],
    metadata: {
      title: "fatal custom level",
    },
    status: "unresolved",
    subscriptionDetails: null,
    isPublic: false,
    hasSeen: false,
    shortId: "DJANGO-G",
    shareId: null,
    firstSeen: "2021-02-19T18:56:01.952Z",
    count: "1",
    permalink: "https://.com",
    level: "fatal",
    isSubscribed: true,
    isBookmarked: false,
    project: {
      platform: "python-django",
      slug: "django",
      id: "21",
      name: "Django",
    },
    statusDetails: {},
  },
  {
    lastSeen: "2021-02-19T18:55:59.366Z",
    numComments: 0,
    userCount: 0,
    stats: {
      "24h": [
        [1613678400, 0],
        [1613682000, 0],
        [1613685600, 0],
        [1613689200, 0],
        [1613692800, 0],
        [1613696400, 0],
        [1613700000, 0],
        [1613703600, 0],
        [1613707200, 0],
        [1613710800, 0],
        [1613714400, 0],
        [1613718000, 0],
        [1613721600, 0],
        [1613725200, 0],
        [1613728800, 0],
        [1613732400, 0],
        [1613736000, 0],
        [1613739600, 0],
        [1613743200, 0],
        [1613746800, 0],
        [1613750400, 0],
        [1613754000, 0],
        [1613757600, 1],
        [1613761200, 0],
      ],
    },
    culprit: "/level-error/",
    title: "error custom level",
    id: 239,
    assignedTo: null,
    logger: null,
    type: "default",
    annotations: [],
    metadata: {
      title: "error custom level",
    },
    status: "unresolved",
    subscriptionDetails: null,
    isPublic: false,
    hasSeen: false,
    shortId: "DJANGO-F",
    shareId: null,
    firstSeen: "2021-02-19T18:55:59.366Z",
    count: "1",
    permalink: "https://.com",
    level: "error",
    isSubscribed: true,
    isBookmarked: false,
    project: {
      platform: "python-django",
      slug: "django",
      id: "21",
      name: "Django",
    },
    statusDetails: {},
  },
  {
    lastSeen: "2021-02-19T18:55:56.932Z",
    numComments: 0,
    userCount: 0,
    stats: {
      "24h": [
        [1613678400, 0],
        [1613682000, 0],
        [1613685600, 0],
        [1613689200, 0],
        [1613692800, 0],
        [1613696400, 0],
        [1613700000, 0],
        [1613703600, 0],
        [1613707200, 0],
        [1613710800, 0],
        [1613714400, 0],
        [1613718000, 0],
        [1613721600, 0],
        [1613725200, 0],
        [1613728800, 0],
        [1613732400, 0],
        [1613736000, 0],
        [1613739600, 0],
        [1613743200, 0],
        [1613746800, 0],
        [1613750400, 0],
        [1613754000, 0],
        [1613757600, 1],
        [1613761200, 0],
      ],
    },
    culprit: "/level-warning/",
    title: "warning custom level",
    id: 238,
    assignedTo: null,
    logger: null,
    type: "default",
    annotations: [],
    metadata: {
      title: "warning custom level",
    },
    status: "unresolved",
    subscriptionDetails: null,
    isPublic: false,
    hasSeen: true,
    shortId: "DJANGO-E",
    shareId: null,
    firstSeen: "2021-02-19T18:55:56.932Z",
    count: "1",
    permalink: "https://.com",
    level: "warning",
    isSubscribed: true,
    isBookmarked: false,
    project: {
      platform: "python-django",
      slug: "django",
      id: "21",
      name: "Django",
    },
    statusDetails: {},
  },
  {
    lastSeen: "2021-02-19T18:55:53.808Z",
    numComments: 0,
    userCount: 0,
    stats: {
      "24h": [
        [1613678400, 0],
        [1613682000, 0],
        [1613685600, 0],
        [1613689200, 0],
        [1613692800, 0],
        [1613696400, 0],
        [1613700000, 0],
        [1613703600, 0],
        [1613707200, 0],
        [1613710800, 0],
        [1613714400, 0],
        [1613718000, 0],
        [1613721600, 0],
        [1613725200, 0],
        [1613728800, 0],
        [1613732400, 0],
        [1613736000, 0],
        [1613739600, 0],
        [1613743200, 0],
        [1613746800, 0],
        [1613750400, 0],
        [1613754000, 0],
        [1613757600, 1],
        [1613761200, 0],
      ],
    },
    culprit: "/level-info/",
    title: "info custom level",
    id: 237,
    assignedTo: null,
    logger: null,
    type: "default",
    annotations: [],
    metadata: {
      title: "info custom level",
    },
    status: "unresolved",
    subscriptionDetails: null,
    isPublic: false,
    hasSeen: false,
    shortId: "DJANGO-D",
    shareId: null,
    firstSeen: "2021-02-19T18:55:53.808Z",
    count: "1",
    permalink: "https://.com",
    level: "info",
    isSubscribed: true,
    isBookmarked: false,
    project: {
      platform: "python-django",
      slug: "django",
      id: "21",
      name: "Django",
    },
    statusDetails: {},
  },
];

export const issueList: Issue[] = apiIssueList.map((apiIssue) => {
  return {
    ...apiIssue,
    project: {
      ...apiIssue.project,
      id: parseInt(apiIssue.project.id, 10),
    },
  };
});
