export const clickAnywhere = (node) => {
  const handleClick = () => {
    if (node) {
      node.dispatchEvent(new CustomEvent('clickAnywhereEvent', node));
    }
  };

  document.addEventListener('click', handleClick);

  return {
    destroy() {
      document.removeEventListener('click', handleClick);
    },
  };
};
