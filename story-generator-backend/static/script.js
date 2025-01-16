// 存储用户选择的数据
let selectedCharacters = [];
let selectedScene = '';

// 动态加载角色和场景
async function loadElements() {
  try {
    const response = await fetch('/api/elements');
    const elements = await response.json();

    // 渲染角色
    const characterContainer = document.querySelector('.character-list');
    for (const [key, value] of Object.entries(elements.characters)) {
      const characterDiv = document.createElement('div');
      characterDiv.className = 'character';
      characterDiv.onclick = () => toggleCharacterSelection(characterDiv, key);

      characterDiv.innerHTML = `
        <img src="${value.image}" alt="${key}" />
        <p>${value.description}</p>
      `;
      characterContainer.appendChild(characterDiv);
    }

    // 渲染场景
    const sceneContainer = document.querySelector('.scene-list');
    for (const [key, value] of Object.entries(elements.scenes)) {
      const sceneDiv = document.createElement('div');
      sceneDiv.className = 'scene';
      sceneDiv.onclick = () => selectScene(sceneDiv, key);

      sceneDiv.innerHTML = `
        <img src="${value.image}" alt="${key}" />
        <p>${value.description}</p>
      `;
      sceneContainer.appendChild(sceneDiv);
    }
  } catch (error) {
    console.error('Failed to load elements:', error);
  }
}

// 选择角色（多选）
function toggleCharacterSelection(element, character) {
  const isSelected = selectedCharacters.includes(character);

  if (isSelected) {
    // 取消选中
    selectedCharacters = selectedCharacters.filter((c) => c !== character);
    element.classList.remove('selected');
  } else {
    // 添加选中
    selectedCharacters.push(character);
    element.classList.add('selected');
  }

  console.log('Selected characters:', selectedCharacters);
}

// 选择场景（单选）
function selectScene(element, scene) {
  // 清除其他选中的场景
  const sceneElements = document.querySelectorAll('.scene');
  sceneElements.forEach((el) => el.classList.remove('selected'));

  // 选中当前场景
  element.classList.add('selected');
  selectedScene = scene;

  console.log('Selected scene:', selectedScene);
}

// 提交请求生成故事
async function generateStory() {
  if (selectedCharacters.length === 0 || selectedScene === '') {
    alert('请选择至少一个角色和一个场景！');
    return;
  }

  try {
    const response = await fetch('/api/generate_story', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        characters: selectedCharacters,
        scene: selectedScene,
      }),
    });

    const data = await response.json();
    if (data.error) {
      alert(`生成失败：${data.error}`);
    } else {
      // 显示生成的故事和音频
      document.getElementById('story').textContent = data.story;
      const audio = document.getElementById('audio');
      audio.src = '/api/play_audio';
      audio.style.display = 'block';
    }
  } catch (error) {
    console.error('Failed to generate story:', error);
    alert('生成故事失败，请检查后端日志！');
  }
}

// 初始化页面
loadElements();
