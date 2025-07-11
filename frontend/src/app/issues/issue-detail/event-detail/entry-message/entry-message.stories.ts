import { EntryMessageComponent } from "./entry-message.component";

import { cspError } from "../test-data/csp-error";
import { signal } from "@angular/core";

export default {
  title: "Events/Event Detail/Entry Message",
  component: EntryMessageComponent,
};

export const EntryMessage = () => {
  return {
    props: {
      eventEntryMessage: signal(cspError.entries[0].data),
    },
  };
};
